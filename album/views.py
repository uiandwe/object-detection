import hashlib
from datetime import datetime

from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.views import View

from .classes.yolo_model import YoloModel
from .forms import PhotoForm
from .models import Photo, Tag
import logging


class IndexView(View):
    def get(self, request, *args, **kwargs):
        d = dict()

        photos = Photo.objects.all()
        for photo in photos:
            d[photo.name] = {"id": photo.id,
                             "tags": [t.name for t in photo.tags.all()]
                             }

        logging.info(dict(d))

        return render(request, 'index.html', {
            'photos': d,
            'tags': [tag.name for tag in Tag.objects.all()]
        })


class PhotoView(View):

    def create_new_file_new(self, file_name):
        name = file_name + str(datetime.now().timestamp())
        md5_result = hashlib.md5(name.encode()).hexdigest()
        return "{file_name}.{extension}".format(file_name=md5_result, extension=file_name.split(".")[-1])

    def post(self, request, *args, **kwargs):

        upload_file = request.FILES
        form = PhotoForm(request.POST, upload_file)
        if form.is_valid():
            file_name = upload_file['photo'].name

            new_file_name = self.create_new_file_new(file_name)

            upload_file['photo'].name = new_file_name
            file_path = "media/photo/{}".format(new_file_name)

            new_photo = Photo(file=upload_file['photo'], name=file_path)
            new_photo.save()

            logging.info(upload_file['photo'].name)

            detect_tags, is_run_models = YoloModel.run(file_path)

            for model, is_run in is_run_models.items():
                new_photo.__dict__[model] = is_run

            new_photo.save()

            logging.info(detect_tags)
            tags = Tag.set_tag(detect_tags)
            for tag in tags:
                new_photo.tags.add(tag)

        else:
            logging.info(form.errors)
            message = 'The form is not valid. Fix the following error:'
        return redirect('index')

    def get(self, request, *args, **kwargs):
        message = 'Upload as many files as you want!'
        form = PhotoForm()
        photos = Photo.objects.all()

        context = {'photos': photos, 'form': form, 'message': message}
        return render(request, 'photo.html', context)


class PhotoDetailView(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id', None)

        try:
            photo = Photo.objects.get(id=id)
        except Photo.DoesNotExist:
            photo = None

        tags = [tag.name for tag in photo.tags.all()]
        photo = model_to_dict(photo)
        logging.info(photo)

        context = {'photo': photo, 'tags': tags, 'filename': photo['name'].split("/")[-1].split(".")[0]}

        return render(request, 'photo_detail.html', context)
