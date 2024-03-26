from django.urls import path, include

from music import views as music_views


urlpatterns = [
    path('category/', music_views.AllCategory.as_view()),
    path('music/', music_views.AllMusicAPIView.as_view()),
    path('music/create/', music_views.CreateMusicAPIView.as_view()),
    path('music/update/<int:pk>/', music_views.EditMusicAPIView.as_view()),
    path('music/delete/<int:pk>/', music_views.DeletMusicAPIView.as_view()),
]
