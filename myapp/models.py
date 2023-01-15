from django.db import models

class Post(models.Model):
    post_id = models.IntegerField("id", 'id', True)
    title = models.CharField("title", 'title', max_length=100)
