from .models import Post, Category
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
