from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('news', views.NewsView)  # news is the endpoint

urlpatterns = [
    path('', include(router.urls))
]
