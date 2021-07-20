from django.urls import path, include
from . import views

urlpatterns = [
    path('shows/new', views.shows),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.one_show),
    path('shows/shows', views.all_shows),
    path('shows/<int:id>/delete', views.delete_show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.update_shows)
]