# Generated by Django 2.0.4 on 2018-05-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='draws',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='victories',
            field=models.IntegerField(default=0),
        ),
    ]
