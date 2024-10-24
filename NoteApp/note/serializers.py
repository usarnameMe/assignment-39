from django.contrib.auth.models import User
from rest_framework import serializers
from NoteApp.note.models import Note
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email"
        ]


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Note
        fields = [
            "id", "title", "body", "user", "slug"
        ]


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'body', 'created_at', 'updated_at']
