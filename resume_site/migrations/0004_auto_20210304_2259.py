# Generated by Django 3.1.2 on 2021-03-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_site', '0003_auto_20210304_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='dateofEnding',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='dateofjoining',
            field=models.DateField(auto_now_add=True),
        ),
    ]
