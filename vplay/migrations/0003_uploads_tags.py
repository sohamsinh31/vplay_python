# Generated by Django 4.0.5 on 2022-08-31 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vplay', '0002_uploads_category_uploads_date_alter_uploads_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='tags',
            field=models.CharField(default=datetime.datetime(2022, 8, 31, 17, 52, 56, 964889, tzinfo=utc), max_length=580),
            preserve_default=False,
        ),
    ]
