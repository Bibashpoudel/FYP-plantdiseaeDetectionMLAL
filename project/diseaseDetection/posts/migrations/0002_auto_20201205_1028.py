# Generated by Django 3.1.2 on 2020-12-05 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_relationship'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]