from django.urls import path
from . import views


urlpatterns = [
    path('motivation/', views.motivation),
    path('job/', views.career),
    path('coding/', views.coding),
]
