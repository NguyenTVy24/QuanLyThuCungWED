from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('connectedMetaMask/', views.connectedMetaMask),
    path('Pets.HTML/', views.petshtml),
    path('checkThuCung/', views.check),
    path('updateThuCung/', views.update),
    path('getfather/<str:pk>', views.getFollowFather),
    path('getmother/<str:pk>', views.getFollowMother),
]


