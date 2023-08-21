from .models import Post, Category
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
