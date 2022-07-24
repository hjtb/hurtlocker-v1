# Generated by Django 3.2.14 on 2022-07-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True, max_length=255)),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
