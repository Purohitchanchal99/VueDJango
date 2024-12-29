from rest_framework import generics, status  # type: ignore # For generic API views and status codes
from rest_framework.pagination import PageNumberPagination  # type: ignore # For paginated responses
from rest_framework.response import Response  # type: ignore # For API responses
from rest_framework.views import APIView  # type: ignore # For custom API views
from .models import Post, Comment
from .serializers import PostSerializer

"""
API Endpoint: /posts/

This endpoint returns a paginated list of posts, with each post containing:
- Post text
- Timestamp
- Author's username
- Comment count
- Up to 3 random comments per post.

Pagination is supported with the following query parameters:
- page_size (optional, default is 10 posts per page)
- page (optional, default is the first page)
"""

# Pagination class for handling pagination of posts
class PostPagination(PageNumberPagination):
    page_size = 10  # Default number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100

# API View for listing posts with random comments
class PostListView(APIView):
    def get(self, request, *args, **kwargs):
        paginator = PostPagination()
        posts = Post.objects.all().order_by('-timestamp')
        paginated_posts = paginator.paginate_queryset(posts, request)

        data = []
        for post in paginated_posts:
            # Fetch random comments
            comments = post.comments.all().order_by('?')[:3]

            data.append({
                'id': post.id,
                'text': post.text,
                'timestamp': post.timestamp,
                'author': post.author.username,
                'comment_count': post.comments.count(),
                'comments': [
                    {
                        'id': comment.id,
                        'text': comment.text,
                        'timestamp': comment.timestamp,
                        'author': comment.author.username,
                    } for comment in comments
                ]
            })

        return paginator.get_paginated_response(data)

# API View for retrieving the details of a single post
class PostDetailAPIView(generics.RetrieveAPIView):
    """
    API Endpoint: /posts/<id>/

    Retrieves the details of a single post by its ID. Includes:
    - Post text
    - Timestamp
    - Author's username
    - Comment count
    - Up to 3 random comments
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Fetch random comments
        comments = instance.comments.all().order_by('?')[:3]

        data = {
            'id': instance.id,
            'text': instance.text,
            'timestamp': instance.timestamp,
            'author': instance.author.username,
            'comment_count': instance.comments.count(),
            'comments': [
                {
                    'id': comment.id,
                    'text': comment.text,
                    'timestamp': comment.timestamp,
                    'author': comment.author.username
                } for comment in comments
            ]
        }
        return Response(data, status=status.HTTP_200_OK)
