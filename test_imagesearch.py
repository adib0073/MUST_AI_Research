'''
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from azure.cognitiveservices.search.imagesearch.models import ImageType, ImageAspect, ImageInsightModule
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "4b9aae1c32e642dab9d96543e4ae0092"

client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

image_results = client.images.search(
        query="Yosemite",
        image_type=ImageType.photo, # Could be the str "AnimatedGif"
        aspect=ImageAspect.all # Could be the str "Wide"
    )
print("\r\nSearch images for \"Yosemite\" results that are animated gifs and wide aspect")

if image_results.value:
    first_image_result = image_results.value[0]
    print("Image result count: {}".format(len(image_results.value)))
    print("First image insights token: {}".format(first_image_result.image_insights_token))
    print("First image thumbnail url: {}".format(first_image_result.thumbnail_url))
    print("First image web search url: {}".format(first_image_result.web_search_url))
else:
    print("Couldn't find image results!")
'''

import requests
import test_edgedetection as startProcess
import sys

subscription_key = "faad681563ad44ffb6c1f9460a9b60a1"
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"


def start(search_term = "satya nadella"):

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "size" : "Large", "color": "monochrome"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    
    content_Url = [img["contentUrl"] for img in search_results["value"][:16]]
    for i in range(1):
        if(i > len(content_Url)):
            break
        startProcess.start(content_Url[i], i+1)

if __name__ == "__main__":
    start(sys.argv[1])
