# Generated by Django 4.1.3 on 2023-03-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
