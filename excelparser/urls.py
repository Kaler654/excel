from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file/<str:filename>/', views.view_file, name='view_file'),
    path('file/<str:filename>/sheet/<str:sheet_name>/', views.view_sheet, name='view_sheet'),
]