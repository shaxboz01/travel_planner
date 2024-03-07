# Generated by Django 5.0.3 on 2024-03-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='price',
            field=models.CharField(default='700 $', max_length=50),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='rating',
            field=models.PositiveIntegerField(max_length=1),
        ),
    ]