# Generated by Django 4.2.1 on 2023-06-01 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_alter_champ_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champ',
            name='age',
        ),
    ]