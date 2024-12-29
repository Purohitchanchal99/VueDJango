# from django.db import models
# from django.contrib.auth.models import User

# class Post(models.Model):
#     text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
#     def __str__(self):
#         return self.text[:50]

#     class Meta:
#         ordering = ['-timestamp']

# class Comment(models.Model):
#     text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

#     def __str__(self):
#         return self.text[:50]

#     class Meta:
#         ordering = ['-timestamp']
# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)  # Make sure this is present

#     class Meta:
#         ordering = ['-timestamp']  # This is optional if you want the default order

#     def comment_count(self):
#         return self.comments.count()

#     def __str__(self):
#         return self.text[:50]
from django.db import models
from django.contrib.auth.models import User

# class Post(models.Model):
#     text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
#     def __str__(self):
#         return self.text[:50]

#     class Meta:
#         ordering = ['-timestamp']

#     def comment_count(self):
#         return self.comments.count()

class Post(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.text[:50]

    def comment_count(self):
        return self.comments.count()

    class Meta:
        ordering = ['-timestamp']
        app_label = 'demo'  # Explicitly setting the app_label

class Comment(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text[:50]

    class Meta:
        ordering = ['-timestamp']
