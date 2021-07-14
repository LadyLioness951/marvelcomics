from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comics/', views.comics_index, name='index'),
    path('comics/<int:comic_id>/', views.comics_detail, name='detail'),
    path('comics/create/', views.ComicCreate.as_view(), name='comic_create'),
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comic_update'),
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comic_delete'),
]