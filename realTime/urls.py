#URLS for realTime app are addded here

from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path(r'home/',views.home),
    path(r'dataDisplay/',views.dataDisplay),
    path(r'dataPost/',views.inData),
    path(r'dataPost/?', views.index),
    path(r'tellResponse/',views.userStart),
    path(r'respondResponse/',views.userResponse),
    path(r'binLevels/',views.returnSix),
    path(r'binLvels/',views.returnSixG),
]
