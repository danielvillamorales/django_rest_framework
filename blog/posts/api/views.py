from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from .serializer import PostSerializer
from .permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category','category__slug']


