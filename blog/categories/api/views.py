from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from categories.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']

