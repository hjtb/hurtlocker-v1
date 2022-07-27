# Generated by Django 3.2.14 on 2022-07-27 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='memberships.membership'),
        ),
    ]
