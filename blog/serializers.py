from rest_framework import serializers

from .models import Hero, Post, Category, PostImage, AboutMe, Paragraph


class SerializerParagraph(serializers.ModelSerializer):

    class Meta:
        model = Paragraph
        fields = "__all__"


class SerializerHero(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class SerializerPostImage(serializers.ModelSerializer):
    post = serializers.CharField(required=False)

    class Meta:
        model = PostImage
        fields = "__all__"


class SerializerPost(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Post
        fields = "__all__"

    post_images = SerializerPostImage(many=True)
    post_paragraph = SerializerParagraph(many=True)

    def create(self, validated_data):
        post_images = validated_data.pop("post_images")
        post_paragraph = validated_data.pop("post_paragraph")
        post_images = post_images[0]

        category_name = validated_data.pop("category")
        category = Category.objects.filter(name=category_name.get("name"))[0]
        print(category)

        post, post_is_create = Post.objects.get_or_create(category=category, **validated_data)
        for para in post_paragraph:
            for p in para.values():
                Paragraph.objects.create(post_id=post.id, p=p)

        post_image, b = PostImage.objects.get_or_create(post_id=post.id, **post_images)

        return Post.objects.get(id=post.id)


class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SerializerAboutMe(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = "__all__"
