# Generated by Django 3.1.3 on 2020-11-06 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
