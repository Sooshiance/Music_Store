from rest_framework import serializers 

from .models import Category, Music


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['pk', 'title', 'category', 'description', 'gener', 'wallpaper']
