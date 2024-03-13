from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS','POST']:
            return True
        return obj.user == request.user

