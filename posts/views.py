from rest_framework.views import APIView, Request, Response, status
from .serializer import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404

class PostView(APIView):
    def get(self, request: Request) -> Response:
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class PostDetailsView(APIView):
    def get(self, request: Request, post_id: int) -> Response:

        post = get_object_or_404(Post, id=post_id)
        
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)