from django.db import models


class Films(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=255, default='')
    producer = models.CharField(null=False, max_length=255, default='')
    duration = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'ID: {self.id} {self.title}'