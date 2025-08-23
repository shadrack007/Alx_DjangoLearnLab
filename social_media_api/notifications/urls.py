from django.urls import path

from .views import UserNotificationView

urlpatterns = [
    path('me', UserNotificationView.as_view(), name = 'user_notifications'),
]
