# Generated by Django 5.0.2 on 2024-03-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
