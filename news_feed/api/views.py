from rest_framework import viewsets
from ..models import Article, News, Rate
from .serializers import ArticleSerializer, NewsSerializer, RateSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class RateView(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
