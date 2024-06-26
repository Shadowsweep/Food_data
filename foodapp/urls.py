from django.urls import path
from . import views

urlpatterns = [
     path('', views.upload_csv),
     path('upload-csv/', views.upload_csv),
     path('display_food/', views.display_food),
     path('view_food/', views.view_food),
]
