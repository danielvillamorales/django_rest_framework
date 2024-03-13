from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly

#class PostApiView(APIView):
#    def get(self, request):
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
#
#    def post(self, request):
#        serializer = PostSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

#class PostViewSet(ViewSet):
#    def list(self, request):
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
#    def retrieve(self, request, pk:int):
#        post = Post.objects.get(pk=pk)
#        serializer = PostSerializer(post)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#    def create(self, request):
#        serializer = PostSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_201_CREATED, data=serializer.data)



class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    
    
