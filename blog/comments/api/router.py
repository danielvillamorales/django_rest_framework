from rest_framework.routers import DefaultRouter
from comments.api.views import CommentApiViewSet

router = DefaultRouter()

router.register(r'comments', CommentApiViewSet, basename='comments')
