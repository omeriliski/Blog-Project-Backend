from django.shortcuts import get_object_or_404
from .models import Like, Post,Comment,PostView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import CommentSerializer, PostSerializer, LikeSerializer,PostViewSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,AllowAny

#post
@api_view(["GET",])
def get_posts(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        # number of posts on a page
        paginator.page_size = 2
        posts = Post.objects.all()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

#for permission
@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def create_post(request):
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Post created successfully"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
def get_post(request,post_id): 
    post = get_object_or_404(Post,id=post_id)
    # can be used for details
    if request.method == "GET":
        serializer =  PostSerializer(post)
        return Response(serializer.data)

@api_view(["PUT","DELETE"])
@permission_classes((IsAuthenticated, ))
def update_delete_post(request,post_id): 
    post = get_object_or_404(Post,id=post_id)     
    if request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        if request.user.id != post.author.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Post updated successfully"
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        if request.user.id != post.author.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# comment
@api_view(["GET"])
def get_comments(request,post_id):
    if request.method == "GET":
        comment = Comment.objects.filter(post=post_id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def create_comment(request,post_id):
    if request.method == "POST":
        post = get_object_or_404(Post,id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            data={
                "message":"Comment created successfully"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# like
@api_view(["GET"])
def get_likes(request,post_id):
    if request.method == "GET":
        like_count = Like.objects.filter(post=post_id).count()
        return Response(like_count)

@api_view(["POST","DELETE"])
@permission_classes((IsAuthenticated, ))
def create_delete_like(request,post_id):
    if request.method == "POST":
        post = get_object_or_404(Post,id=post_id)
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            data={
                "message":"Comment created successfully"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        like = Like.objects.filter(post=post_id,user=request.user)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# postview
@api_view(["GET"])
def get_postviews(request,post_id):
    if request.method == "GET":
        postview_count = PostView.objects.filter(post=post_id).count()
        return Response(postview_count)

@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def create_postview(request,post_id):
    if request.method == "POST":
        post = get_object_or_404(Post,id=post_id)
        serializer = PostViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            data={
                "message":"Comment created successfully"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)