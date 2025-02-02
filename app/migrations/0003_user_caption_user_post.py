# Generated by Django 5.0.2 on 2024-02-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_bio_alter_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
