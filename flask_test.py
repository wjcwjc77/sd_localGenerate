from flask import Flask, jsonify, request, render_template
import json
import requests
import io
import base64
from PIL import Image
from flask_cors import CORS

url = "http://127.0.0.1:7860"
app = Flask(__name__)
# 实现跨域

CORS(app, supports_credentials=True)

@app.route('/test', methods=['post'])
def test():
    data = request.get_json(silent=True)
    print(data["payload"])
    if data != {}:
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=data["payload"])
        r = response.json()
        print(r)
        for i in r['images']:
            image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
            image.save('output.png')
            # imgBs4 = base64.b64encode(image).decode()
    # 读取图片，返回给前端
    path = "output.png"
    fileOpen = open(path, 'rb')
    imgBs4 = base64.b64encode(fileOpen.read()).decode()
    return imgBs4


if __name__ == '__main__':
    app.run()

