from rest_framework import serializers
from .models import Post


#I learned that serializer is like my translator..

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'