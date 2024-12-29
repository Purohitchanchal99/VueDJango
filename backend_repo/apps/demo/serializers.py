from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'author']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'author', 'comment_count', 'comments']

    def get_comment_count(self, obj):
        # Call the model method to get the comment count
        return obj.comments.count()

    def get_comments(self, obj):
        # Fetch up to 3 latest comments for the post
        comments = obj.comments.all().order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data
from random import sample

class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'author', 'comment_count', 'comments']

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        comments = obj.comments.order_by('-timestamp')  # Sort comments by timestamp
        return CommentSerializer(comments[:3], many=True).data  # Return up to 3 comments
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-timestamp')  # Order posts by timestamp
    serializer_class = PostSerializer  # Make sure you have a serializer for the Post model