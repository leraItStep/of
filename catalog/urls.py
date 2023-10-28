from django.contrib import admin
from django.urls import path

from catalog import views


urlpatterns = [
    path('', views.catalog_view),
    path('<str:cat>/', views.catalog_detail_view),
    path('<str:cat>/<int:mov_id>/', views.movie_detail_view),
]
