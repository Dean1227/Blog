from django.db import models

from user.models import User


class Category(models.Model):
    c_name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, null=True)
    p_node = models.CharField(max_length=255, null=True)
    c_keyword = models.CharField(max_length=255, null=True)
    c_desc = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'category'


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='upload', null=True)
    content = models.CharField(max_length=5000, null=True)
    cate = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL,
                             related_name='art')
    a_keyword = models.CharField(max_length=255, null=True)
    tag = models.CharField(max_length=255, null=True)
    a_desc = models.CharField(max_length=255, null=True)
    is_open = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'


class MessageBook(models.Model):

    name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=3000, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'message_book'






