# Generated by Django 4.0.5 on 2022-08-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=355)),
                ('vidpath', models.CharField(max_length=255)),
                ('thumbpath', models.CharField(max_length=255)),
                ('uploadby', models.CharField(max_length=255)),
            ],
        ),
    ]
