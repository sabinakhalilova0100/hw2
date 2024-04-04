from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'ID: {self.id} {self.name}'


class List(models.Model):
    title = models.CharField(null=False, max_length=255,default='')
    description = models.CharField(null=False, max_length=3000,default='')
    due_date = models.DateField(null=False, blank=False)
    status = models.BooleanField(null=False, default=False)


def __str__(self):
    return f'ID:{self.id} {self.title}'


class BasketItem(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(List, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, default=1)

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'

    def __str__(self):
        return f'ID: {self.id} {self.owner} {self.product.name} {self.amount}'