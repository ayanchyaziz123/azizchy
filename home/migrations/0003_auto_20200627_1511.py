# Generated by Django 3.0.7 on 2020-06-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postText',
            new_name='postInPython',
        ),
        migrations.AddField(
            model_name='post',
            name='postInC',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='postInCplus',
            field=models.TextField(default=11.11),
            preserve_default=False,
        ),
    ]