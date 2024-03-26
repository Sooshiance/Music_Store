from django.urls import path, include

from user import views as user_views
from music import views as music_views


urlpatterns = [
    # TODO : 
    path('user/token/', user_views.LoginAPIView.as_view()),
    path('user/token/otp/', user_views.OTPLoginVerifyAPIView.as_view()),
    path('user/register/', user_views.RegisterAPIView.as_view()),
    path('user/register/otp/', user_views.OTPRegisterVerifyAPIView.as_view()),
    path('profile/update/', user_views.ProfileAPIView.as_view()),

    # TODO :
    path('category/', music_views.AllCategory.as_view()),
    path('music/', music_views.AllMusicAPIView.as_view()),
    path('music/<int:pk>/', music_views.SingleMusicAPIView.as_view()),
    path('music/create/', music_views.CreateMusicAPIView.as_view()),
    path('music/update/<int:pk>/', music_views.EditMusicAPIView.as_view()),
    path('music/delete/<int:pk>/', music_views.DeletMusicAPIView.as_view()),
    path('music/search/', music_views.SearchMusicAPIVIew.as_view()),
]
