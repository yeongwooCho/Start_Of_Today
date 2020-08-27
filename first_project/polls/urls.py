from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('page2', views.motivation),
    path('page3', views.career),
    path('page4', views.coding),
]
