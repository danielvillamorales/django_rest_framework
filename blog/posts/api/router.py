from rest_framework.routers import DefaultRouter
from .views import PostApiViewSet

router = DefaultRouter()

router.register(r'posts', PostApiViewSet, basename='posts')
