from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField


class Article(models.Model):
    article_name = models.CharField(max_length=50)
    content = models.CharField(max_length=256)
    author_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.article_name


class News(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.name

MY_RATES = (
    (1, 'Fair'),
    (2, 'Not Bad'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'))


class Rate(models.Model):
    rate_title = models.CharField(max_length=50)
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    rate = MultiSelectField(choices=MY_RATES, default='Fair')
    date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.rate_title
