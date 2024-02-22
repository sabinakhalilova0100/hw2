from django.db import models


class List(models.Model):
    title = models.CharField(null=False, max_length=255,default='')
    description = models.CharField(null=False, max_length=3000,default='')
    due_date = models.DateField(null=False, blank=False)
    status = models.BooleanField(null=False, blank=False)


    def __str__(self):
        return f'ID:{self.id} {self.title}'
