# Generated by Django 4.1.7 on 2023-03-29 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_userprofile_language_userprofile_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='language',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German')], default=True, max_length=2),
        ),
    ]