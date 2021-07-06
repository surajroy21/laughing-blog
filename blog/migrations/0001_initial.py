# Generated by Django 3.2.5 on 2021-07-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('draft', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
