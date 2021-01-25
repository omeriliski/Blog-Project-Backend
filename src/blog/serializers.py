from django.db import models
from rest_framework import serializers
from .models import Post, Comment,Like, PostView

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","content","image","category","publish_date","last_updated","author","slug"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Comment
        fields=["content"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Like
        fields=[]
    
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PostView
        fields=[]