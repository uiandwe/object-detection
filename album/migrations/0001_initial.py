# Generated by Django 3.2.5 on 2021-07-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('file', models.ImageField(upload_to='photo')),
                ('tags', models.TextField(default='')),
            ],
        ),
    ]
