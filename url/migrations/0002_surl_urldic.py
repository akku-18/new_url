# Generated by Django 2.2.12 on 2022-10-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surl',
            name='urldic',
            field=models.CharField(default='nothing', max_length=100),
        ),
    ]
