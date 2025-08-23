from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        user_to_follow = get_object_or_404(User, id = user_id)

        # Prevent from self following
        if current_user == user_to_follow:
            return Response(
                {"error": "You cannot follow yourself."},
                status = status.HTTP_400_BAD_REQUEST
            )

        # prevent following already followed users
        if user_to_follow in current_user.following.all():
            return Response(
                {"error": "You already follow this user."},
                status = status.HTTP_400_BAD_REQUEST
            )
        # Add user
        request.user.follow(user_to_follow)
        return Response(
            {
                'message': f'You are now following {user_to_follow.username}',

            }, status = status.HTTP_200_OK
        )


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        user_to_unfollow = get_object_or_404(User, id = user_id)

        # prevent unfollowing if not following
        if user_to_unfollow not in current_user.following.all():
            return Response(
                {"error": "You are not following this user."},
                status = status.HTTP_400_BAD_REQUEST
            )
        # Remove following
        request.user.unfollow(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"}, status = status.HTTP_200_OK)
