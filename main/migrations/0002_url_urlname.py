# Generated by Django 3.1.2 on 2021-04-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='urlName',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
