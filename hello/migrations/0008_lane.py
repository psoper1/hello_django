# Generated by Django 4.2.1 on 2023-06-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_champ_splash'),
    ]

    operations = [
        migrations.CreateModel(
            name='lane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lane', models.CharField(max_length=100)),
            ],
        ),
    ]
