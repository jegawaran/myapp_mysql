# Generated by Django 3.0.5 on 2020-06-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetailapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='Steve Jobs', max_length=200),
        ),
    ]
