# Generated by Django 3.2.4 on 2021-09-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='option',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
