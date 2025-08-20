from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegisterSerializer, SimpleProfileSerializer

User = get_user_model()


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    print('called', queryset)


class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = SimpleProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
