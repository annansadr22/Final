# Generated by Django 4.1.7 on 2023-03-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0007_remove_userprofile_language_userprofile_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default=None, max_length=100),
        ),
    ]