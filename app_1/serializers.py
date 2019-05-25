from rest_framework import serializers
from app_1 import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blogs
        fields = '__all__'


class Blogs_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blogs
        fields = '__all__'