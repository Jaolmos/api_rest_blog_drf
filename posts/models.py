from django.db import models
from users.models import User
from categories.models import Category
from django.db.models import SET_NULL


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    thumbnail = models.ImageField(upload_to='posts/img')
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    published = models.BooleanField(default=False)
    # Relación uno a muchos con user como ForeignKey. Si se elimina el usuario, el post no se elimina. 
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    # Relación uno a muchos con category como ForeignKey. Si se elimina una categoria, el post no se elimina.
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

