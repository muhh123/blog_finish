from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


#I learned that serializer is like my translator..
#make posts into json
class PostSerializer(serializers.ModelSerializer):
   
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author']
        read_only_fields = ['id', 'created_at', 'author']






class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user