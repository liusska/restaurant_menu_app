# Generated by Django 4.0.4 on 2022-05-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
                ('ingredients', models.TextField()),
                ('cooking_time', models.IntegerField(default=0)),
                ('description', models.TextField()),
            ],
        ),
    ]
