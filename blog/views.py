from rest_framework import viewsets

from .models import Hero , Post ,Category ,PostImage ,AboutMe
from .serializers import SerializerHero , SerializerPost ,SerializerCategory ,SerializerPostImage ,SerializerAboutMe


class ViewHero(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = SerializerHero


class ViewPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = SerializerPost


class ViewCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = SerializerCategory


class ViewPostImage(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = SerializerPostImage


class ViewAboutMe(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = SerializerAboutMe

