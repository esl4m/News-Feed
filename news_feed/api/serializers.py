from rest_framework import serializers
from news_feed.models import Article, News, Rate


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'article_name', 'author_name', 'date')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'name', 'description', 'article_id', 'date')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'rate_title', 'article_id', 'rate', 'date')
