from rest_framework import serializers
from .models import Post


class PostSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']
