from django.urls import path
from .views import *
from main import views

urlpatterns = [
    path('', views.index_view.as_view(), name='index')
]