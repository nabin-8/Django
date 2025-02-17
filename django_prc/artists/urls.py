from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = views.custom_page_not_found

urlpatterns = [
    path("", views.index, name="index"),
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artists/new/', views.artist_create, name='artist_create'),
    path('artists/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
    path('artists/<int:pk>/delete/', views.artist_delete, name='artist_delete'),
]
