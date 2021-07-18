from django.db import models

# Create your models here.
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def set_tag(tags):
        assert type(tags) == list

        ret = []
        for t in tags:
            try:
                tag = Tag.objects.get(name=t)
            except Tag.DoesNotExist as e:
                tag = Tag(name=t)
                tag.save()
            ret.append(tag)
        return ret

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.TextField(default='')
    file = models.ImageField(null=False, upload_to="photo")
    is_run_gun_model = models.BooleanField(default=False)
    is_run_fruit_model = models.BooleanField(default=False)
    is_run_plant_model = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    @staticmethod
    def save_tags(photo, tag):
        try:
            photo.tags.add(tag)
            photo.save()
        except Exception as e:
            print(e)


    @staticmethod
    def get_all_photos():
        p = Photo.objects.all()
        print(p[3].tags.all())

    def __str__(self):
        return self.name
