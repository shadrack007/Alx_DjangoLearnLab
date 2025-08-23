from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, FeedView, PostLikeView, PostUnlikeView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name = 'user_feed'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name = 'post_like'),
    path('posts/<int:pk>/unlike/', PostUnlikeView.as_view(), name = 'post_unlike'),
]
