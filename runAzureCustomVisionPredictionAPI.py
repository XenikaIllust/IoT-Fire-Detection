import http.client, urllib.request, urllib.parse, urllib.error, base64
from PIL import Image
import os

headers = {
    # Request headers
    'Prediction-Key': '',
    'Content-Type': 'multipart/form-data',
    'Prediction-key': '****************************',
}

params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': '',
    'application': '',
})


while file in os.listdir("data"):
    image = open("./data/" + file, "rb")
    print(file)

    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v2.0/Prediction/*******************************/image?%s" % params, image, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    image.close()

####################################
#powered by Microsoft Azure