from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('motivation/', views.motivation),
    path('job/', views.career),
    path('coding/', views.coding),
]
