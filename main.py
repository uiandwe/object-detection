# -*- coding: utf-8 -*-
import json
from glob import glob

import torch
from flask import Flask, render_template

app = Flask(__name__)
db = {}


def make_db():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    with open('tags_ko.json') as f:
        tags_ko = json.load(f)

    img_list = glob('static/photos/*.jpg')

    for img_path in img_list:
        results = model(img_path)

        tags = set()

        for pred in results.pred[0]:
            tag = tags_ko[int(pred[-1])]
            tag = tag.replace(' ', '')
            tags.add(tag)

        db[img_path] = list(tags)

make_db()

@app.route('/')
def index():
    return render_template('index.html', photos=db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
