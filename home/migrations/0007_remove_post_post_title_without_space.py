# Generated by Django 3.0.7 on 2020-06-27 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_title_without_space',
        ),
    ]
