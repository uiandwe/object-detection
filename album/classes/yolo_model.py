# -*- coding: utf-8 -*-
import json

import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
gun_model = torch.hub.load('ultralytics/yolov5', 'custom', path='train/gun_yolov5s_results/weights/best.pt')
fruit_model = torch.hub.load('ultralytics/yolov5', 'custom', path='train/fruit_yolov5s_results/weights/best.pt')
plant_model = torch.hub.load('ultralytics/yolov5', 'custom', path='train/plant_yolov5s_results/weights/best.pt')


class YoloModel:
    models = {
        'gun': gun_model,
        'fruit': fruit_model,
        'plant_mode': plant_model
    }

    @staticmethod
    def set_run_model(model, file_path):
        r = model(file_path)
        if len(r.pred[0]) > 0:
            return r
        return None

    @staticmethod
    def run(file_path):
        with open('tags_ko.json') as f:
            tags_ko = json.load(f)
        results = model(file_path)
        results.save("media/photo/detect/")

        tags = set()
        is_run_models = dict()

        for pred in results.pred[0]:
            tag = tags_ko[int(pred[-1])]
            tag = tag.replace(' ', '')
            tags.add(tag)

        # for model_name in YoloModel.models:
        #     m = YoloModel.models[model_name]
        #
        #     YoloModel.set_run_model(m, file_path)
        r = gun_model(file_path)
        if len(r.pred[0]) > 0:
            r.save("media/photo/detect/gun/")
            is_run_models['is_run_gun_model'] = True

        f = fruit_model(file_path)
        if len(f.pred[0]) > 0:
            f.save("media/photo/detect/fruit/")
            is_run_models['is_run_fruit_model'] = True

        p = plant_model(file_path)
        if len(p.pred[0]) > 0:
            p.save("media/photo/detect/plant/")
            is_run_models['is_run_plant_model'] = True

        return list(tags), is_run_models
