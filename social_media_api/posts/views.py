from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment, Like

from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # automatically set the logged in user as the author
        serializer.save(author = self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the logged in user as the authro
        serializer.save(author = self.request.user)


class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # get all users the current user follows
        following_users = user.following.all()
        feeds = Post.objects.filter(author__in = following_users).order_by
        return feeds


class PostLikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk = pk)
        user = request.user

        #     handle duplicate like
        if Like.objects.filter(user = user, post = post).exists():
            return Response({"error": "You already liked this post."}, status = status.HTTP_400_BAD_REQUEST)
        else:
            Like.objects.get_or_create(user = user, post = post)
            # generate like notification
            if post.author != user:  # prevent self notification
                Notification.objects.create(
                    recipient = post.author,
                    actor = user,
                    verb = 'liked',
                    target = post
                )
            return Response({"message": f"You liked post {post.id}."}, status = status.HTTP_200_OK)


class PostUnlikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        post = generics.get_object_or_404(Post, pk = pk)

        # check if like exists
        like = Like.objects.filter(user = user, post = post).first()

        if not like:
            return Response(
                {
                    'error': 'You have not liked this post',
                }, status = status.HTTP_400_BAD_REQUEST
            )
        like.delete()

        # generate unlike notification
        if post.author != user:  # prevent self-notification
            Notification.objects.create(
                recipient = post.author,
                actor = user,
                verb = "unliked",
                target = post
            )
        return Response({"message": f"You unliked post {post.id}."}, status = status.HTTP_200_OK)
