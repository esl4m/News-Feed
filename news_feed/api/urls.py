from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('articles', views.ArticleView)
router.register('news', views.NewsView)
router.register('rates', views.RateView)

urlpatterns = [
    path('', include(router.urls))
]
