# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('photo/', views.PhotoView.as_view(), name='photo'),
    path('photo/<int:id>/', views.PhotoDetailView.as_view(), name='photo_detail')
]
