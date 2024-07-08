from rest_framework import serializers
from api.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
