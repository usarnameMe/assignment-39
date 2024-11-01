# note/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'slug', 'user']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ["id", "owner", "title", "body", "created_at", "updated_at"]
