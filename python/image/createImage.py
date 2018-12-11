import requests
import base64
import json
import configparser
import sys
import os.path

libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])

from auth import auth

config = configparser.ConfigParser()
config.read('../config.ini')
apiKey = config['AUTH']['ApiKey']
apiSecret = config['AUTH']['ApiSecret']

if __name__ == '__main__':
    with open('testImage.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    data = {
        'image': str(encoded_string)[2:-1]
    }
    res = requests.post(config['SERVER']['IMGURI'] + '/images',
                        headers=auth.get_headers(apiKey, apiSecret),
                        json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
