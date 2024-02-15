from django.db import models


class Article(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    text = models.CharField(null=False, max_length=255, default='')
    author = models.CharField(null=False, max_length=255, default='')

    def __str__(self):
        return f'ID: {self.id} {self.title}'