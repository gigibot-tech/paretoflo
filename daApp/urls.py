from django.contrib import admin
from django.urls import path
from daApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
]
