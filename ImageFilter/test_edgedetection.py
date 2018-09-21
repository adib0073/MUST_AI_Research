# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:08:55 2018

@author: aaygupta
"""

import cv2
import numpy as np
from pencilsketch import PencilSketch
from PIL import Image
import requests
from io import BytesIO
import sys

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (1.0,1.0,1.0) # In BGR format

def edge_detect(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #-- Edge detection -------------------------------------------------------------------
    edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)
    
    #-- Find contours in edges, sort by area ---------------------------------------------
    contour_info = []
    im2,contours,hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]
    
    #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
    # Mask is black, polygon is white
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))
    
    #-- Smooth mask, then blur it --------------------------------------------------------
    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
    mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
    mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask
    
    #-- Blend masked img into MASK_COLOR background --------------------------------------
    mask_stack  = mask_stack.astype('float32') / 255.0          # Use float matrices, 
    img         = img.astype('float32') / 255.0                 #  for easy blending
    
    masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR) # Blend
    masked = (masked * 255).astype('uint8')                     # Convert back to 8-bit 
    return masked

def remove_background(index =1):
    resultimg = Image.open('person-masked.png');
    resultimg = resultimg.convert("RGBA")
    datas = resultimg.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    resultimg.putdata(newData)
    resultimg.save("final_result"+str(index)+".png", "PNG")#converted Image name
    return resultimg

def start(url, index = 1):
    #for url

    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGB')
    open_cv_image = np.array(img) 
    img = open_cv_image[:, :, ::-1].copy() 
    cv2.imwrite("Source"+str(index)+".jpg", img)
    #img = cv2.imread('C:/temp/kl2.jpg')
    #Apply edge detection
    #img = edge_detect(img)
    #Apply pencil sketch filter
    imgHeight, imgWidth = img.shape[:2]
    pencil_sketch = PencilSketch(imgWidth, imgHeight)
    finalimg = pencil_sketch.render(img, 91,91)
    #finalimg = pencil_sketch.render(finalimg, 1, 251)
    #finalimg = edge_detect(finalimg);
    cv2.imwrite('person-masked.png', finalimg)           # Save
    #Add transparent background
    remove_background(index)
    '''
    open_cv_image = np.array(result1) 
    img = open_cv_image[:, :, ::-1].copy() 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('C:/temp/final_result_opening.png', opening)           # Save
    '''
    
if __name__ == "__main__":
    #remove_background();
    start(sys.argv[1])
    #start('https://pbs.twimg.com/profile_images/988775660163252226/XpgonN0X.jpg')



