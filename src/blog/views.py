from django.shortcuts import get_object_or_404
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework import status

@api_view(["GET","POST"])
def post_list_create(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Post created successfully"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def post_update_delete(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == "GET":
        serializer =  PostSerializer(post)
        return Response(serializer.data)
        
    if request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Post updated successfully"
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
