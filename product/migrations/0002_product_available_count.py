# Generated by Django 4.2 on 2023-06-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_count',
            field=models.IntegerField(default=0),
        ),
    ]
