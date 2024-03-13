from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router_post = DefaultRouter()

router_post.register(r'posts', PostModelViewSet, basename='posts')