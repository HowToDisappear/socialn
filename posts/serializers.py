from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(
        many=True,
        required=False,)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'created', 'modified', 'title', 'body', 'likes']
        extra_kwargs = {
            'id': {'read_only': True},
            'likes': {'read_only': True},}


class LikesSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    likes = serializers.IntegerField()
