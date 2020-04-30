from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ViewHero , ViewPost , ViewCategory ,ViewPostImage ,ViewAboutMe

router = DefaultRouter()

router.register("hero" ,ViewHero)
router.register("post" ,ViewPost)
router.register("category" ,ViewCategory)
router.register("post-image" ,ViewPostImage)
router.register("about-me" ,ViewAboutMe)

urlpatterns = [] 

urlpatterns += router.urls
