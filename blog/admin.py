from django.contrib import admin

from .models import Hero,Category,Post,PostImage,AboutMe

admin.site.register(Hero)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(AboutMe)