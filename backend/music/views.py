from rest_framework import generics, permissions, filters

from .models import Category, Music
from .serializers import CategorySerializer, MusicSerializer


class AllCategory(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AllMusicAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset= Music.objects.all()
    serializer_class = MusicSerializer


class SingleMusicAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MusicSerializer
    lookup_url_kwarg = 'slug'


class CreateMusicAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset= Music.objects.all()
    serializer_class = MusicSerializer


class EditMusicAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class DeletMusicAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Music.objects.all()
    serializer_class = [MusicSerializer]


class SearchMusicAPIVIew(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'user']
