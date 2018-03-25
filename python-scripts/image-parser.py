import io
import os
from jsonparser import parse_json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def detect_document_uri(uri):
    """Detects document features in the file located in Google Cloud
    Storage."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    print("===========================\n", client)

    response = client.document_text_detection(image=image)
    # test = response['full_text_annotation']
    return parse_json(response)

print(detect_document_uri("https://i2.wp.com/thekoreankitchensf.com/wp-content/uploads/2017/04/menu2017revised3.jpg"))
