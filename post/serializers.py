from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        post = Post.objects.create(
            user=self.context['request'].user, **validated_data)
        return post
