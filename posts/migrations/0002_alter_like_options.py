# Generated by Django 4.2.1 on 2023-05-23 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['created_date']},
        ),
    ]
