from django.test import TestCase
from django.contrib.auth.models import User
from demo.models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        # Create a user to associate with the post
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_creation(self):
        # Create a post
        post = Post.objects.create(author=self.user, text='Test Post')
        
        # Check if the post is saved correctly
        self.assertEqual(post.text, 'Test Post')
        self.assertEqual(post.author, self.user)

    def test_comment_count(self):
        post = Post.objects.create(author=self.user, text='Test Post for Comments')
        comment1 = Comment.objects.create(post=post, author=self.user, text='Test Comment 1')
        comment2 = Comment.objects.create(post=post, author=self.user, text='Test Comment 2')

        # Check if the comment count method works
        self.assertEqual(post.comment_count(), 2)


class CommentModelTest(TestCase):
    def setUp(self):
        # Create a user and a post
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(author=self.user, text='Test Post for Comments')

    def test_comment_creation(self):
        # Create a comment
        comment = Comment.objects.create(post=self.post, author=self.user, text='Test Comment')
        
        # Check if the comment is saved correctly
        self.assertEqual(comment.text, 'Test Comment')
        self.assertEqual(comment.post, self.post)
