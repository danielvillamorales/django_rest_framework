from rest_framework import serializers
from comments.models import Comment
from posts.api.serializer import PostSerializer
from users.api.serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'user', 'post')
