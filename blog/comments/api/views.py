from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializer import CommentSerializer
from rest_framework.filters import  OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadOnly

class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = ( OrderingFilter, DjangoFilterBackend)
    ordering = ('-created_at',)
    filterset_fields = ('user__username', 'post__slug','post')
    permission_classes = [IsOwnerOrReadOnly]
    
