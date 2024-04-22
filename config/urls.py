
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mymunkalap_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/megrendelok/', views.MegrendeloListCreate.as_view()),
    path('api/megrendelok/<int:pk>/', views.MegrendeloRetrieveUpdateDestroy.as_view()),
    path('api/hibatipusok/', views.HibatipusokListCreate.as_view()),
    path('api/hibatipusok/<int:pk>/', views.HibatipusokRetrieveUpdateDestroy.as_view()),
    path('api/munkalapok/', views.MunkalapListCreate.as_view()),
    path('api/munkalapok/<int:pk>/', views.MunkalapRetrieveUpdateDestroy.as_view()),
  
    path('api/munkalapAktiv/', views. AktivMunkalapokJsonView.as_view()),
    path('api/munkalapInAktiv/', views. InAktivMunkalapokJsonView.as_view()), 
    path('api/munkalapOsszes/', views. OsszesMunkalapokJsonView.as_view()), 
]