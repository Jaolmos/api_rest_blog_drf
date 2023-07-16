from django.db import models
from django.db.models import CASCADE
from posts.models import Post
from users.models import User


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE)

