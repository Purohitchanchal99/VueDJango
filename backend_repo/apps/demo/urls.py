from django.urls import path  # type: ignore # For URL routing
from .views import PostListView, PostDetailAPIView  # Import the views

urlpatterns = [
    # URL for listing all posts with optional pagination and random comments
    path('posts/', PostListView.as_view(), name='post-list'),

    # URL for retrieving details of a specific post by its ID
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
]
