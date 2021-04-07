import io
import json
#import cv2
import numpy as np
import requests

#img = cv2.imread("a.jpg")
#height, width, _ = img.shape

# Cutting image
#roi = img[0: height, 400: width]

# Ocr
url_api = "https://api.ocr.space/parse/image"
#_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
#file_bytes = io.BytesIO(compressedimage)
with open('a.png', 'rb') as f:
    result = requests.post(url_api,
                files = {'abc.png': f},
                data = {"apikey": "bf7420f44f88957",
                        "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")

print(text_detected)