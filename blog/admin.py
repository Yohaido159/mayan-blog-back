from django.contrib import admin

from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Hero, Category, Post, PostImage, AboutMe, Paragraph

from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class ImagePostInline(admin.TabularInline):
    model = PostImage
    extra = 0


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1


class AdminPost(admin.ModelAdmin):
    inlines = (ImagePostInline, ParagraphInline)


class AdminCategory(admin.ModelAdmin):
    inlines = (PostInline,)


admin.site.register(Hero)
admin.site.register(Paragraph)
admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
admin.site.register(PostImage)
admin.site.register(AboutMe)
