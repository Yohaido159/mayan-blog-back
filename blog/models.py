from datetime import datetime

from django.db import models

def get_post_title(instance, filename):
    return f"post_photo/{instance.post.title}/{filename}"

def get_category_name(instance, filename):
    return f"categories_photo/{instance.name}/{filename}"


class Hero(models.Model):
    hero_image_big = models.ImageField(upload_to="hero_images/%Y/%m/big")
    hero_image_small1 = models.ImageField(upload_to="hero_images/%Y/%m/small1")
    hero_image_small2 = models.ImageField(upload_to="hero_images/%Y/%m/small2")

    def __str__(self):
        return f"hero {self.id}"

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name  = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to=get_category_name)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.title



class PostImage(models.Model):
    post_image = models.ImageField(upload_to=get_post_title)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title
    

class AboutMe(models.Model):
    class Meta:
        verbose_name_plural = "AboutMe"

    image = models.ImageField(upload_to='about_me')
    content = models.TextField()

    def __str__(self):
        return "MAYAN"


    