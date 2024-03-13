from rest_framework.serializers import ModelSerializer
from posts.models import Post
from users.api.serializer import UserSerializer
from categories.api.serializer import CategorySerializer


class PostSerializer(ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category')
        