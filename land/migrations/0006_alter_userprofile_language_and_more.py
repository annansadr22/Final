# Generated by Django 4.1.7 on 2023-03-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0005_remove_userprofile_language_userprofile_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German')], default=False, max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]