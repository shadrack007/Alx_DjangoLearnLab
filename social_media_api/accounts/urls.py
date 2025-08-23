from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name = 'user_register'),
    path('login/', obtain_auth_token, name = 'login'),
    path('profile/', views.UserProfileView.as_view(), name = 'user_Profile'),
    path("follow/<int:user_id>/", views.FollowUserView.as_view(), name = "follow-user"),
    path("unfollow/<int:user_id>/", views.UnfollowUserView.as_view(), name = "unfollow-user"),

]
