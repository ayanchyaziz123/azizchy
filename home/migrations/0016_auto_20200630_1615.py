# Generated by Django 3.0.7 on 2020-06-30 10:15

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_post_cat_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat_search',
            field=models.CharField(default=django.db.models.fields.Field.value_from_object, max_length=200),
        ),
    ]
