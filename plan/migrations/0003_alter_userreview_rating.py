# Generated by Django 5.0.3 on 2024-03-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_accommodation_price_alter_userreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]