# Generated by Django 5.0.2 on 2024-02-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_list_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
