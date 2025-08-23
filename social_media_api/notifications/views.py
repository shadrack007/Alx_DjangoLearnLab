from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .models import Notification
from .serializers import NotificationSerializer


# Create your views here.
class UserNotificationView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient = user).order_by('-timestamp')
