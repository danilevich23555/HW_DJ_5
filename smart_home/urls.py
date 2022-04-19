"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from measurement.views import smart_house_api, smart_house_api_id, Measurements_api
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', smart_house_api.as_view()),
    path('sensors/<pk>/', smart_house_api_id.as_view()),# подключаем маршруты из приложения measurement
    path('measurements/', Measurements_api.as_view()),

]