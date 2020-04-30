from rest_framework import serializers

from .models import Hero,Post,Category,PostImage,AboutMe


class SerializerHero(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"

        
class SerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

        
class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

        
class SerializerPostImage(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"

        
class SerializerAboutMe(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = "__all__"
