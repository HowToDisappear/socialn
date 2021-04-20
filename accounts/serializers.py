from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'posts']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},}
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
