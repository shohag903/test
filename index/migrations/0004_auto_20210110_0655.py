# Generated by Django 3.1.4 on 2021-01-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='link',
            field=models.URLField(max_length=400),
        ),
    ]