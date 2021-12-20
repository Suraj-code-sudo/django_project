# Generated by Django 3.2.4 on 2021-09-15 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_server_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='option',
            new_name='op1',
        ),
        migrations.AddField(
            model_name='server',
            name='op2',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='op3',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='op4',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
