# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:19:22 2018

@author: aaygupta
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

class PencilSketch:
    """Pencil sketch effect
        A class that applies a pencil sketch effect to an image.
        The processed image is overlayed over a background image for visual
        effect.
    """

    def __init__(self, width, height, bg_gray='sketch_bg4.jpg'):
        """Initialize parameters
            :param (width, height): Image size.
            :param bg_gray: Optional background image to improve the illusion
                            that the pencil sketch was drawn on a canvas.
        """
        self.width = width
        self.height = height

        # try to open background canvas (if it exists)
        self.canvas = cv2.imread(bg_gray, cv2.CV_8UC1)
        if self.canvas is not None:
            self.canvas = cv2.resize(self.canvas, (self.width, self.height))

    def render(self, img_rgb, x, y):
        """Applies pencil sketch effect to an RGB image
            :param img_rgb: RGB image to be processed
            :returns: Processed RGB image
        """
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (x, y), 0, 0)
        img_blend = cv2.divide(img_gray, img_blur, scale=256)
        #img_blend = cv2.equalizeHist(img_blend)
        # if available, blend with background canvas
        if self.canvas is not None:
            img_blend = cv2.multiply(img_blend, self.canvas, scale=1./256)

        return img_blend
        #return cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)

'''    
def start(url):
    #for url
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGB')
    open_cv_image = np.array(img) 
    img = open_cv_image[:, :, ::-1].copy() 
    cv2.imwrite("c:\\temp\\Source.jpg", img)
    #img = cv2.imread(url);
    imgHeight, imgWidth = img.shape[:2]
    pencil_sketch = PencilSketch(imgWidth, imgHeight)
    finalimg = pencil_sketch.render(img)
    cv2.imwrite("c:\\temp\\Result.jpg", finalimg)
    return "success"
    
if __name__ == "__main__":
    start(sys.argv[1])
'''
