# Generated by Django 3.1.5 on 2021-02-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeti_app', '0003_auto_20210205_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
