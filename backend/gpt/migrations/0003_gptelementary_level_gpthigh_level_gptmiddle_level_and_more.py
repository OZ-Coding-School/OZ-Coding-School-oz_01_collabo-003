# Generated by Django 5.0.3 on 2024-04-17 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt', '0002_gpttoeic'),
    ]

    operations = [
        migrations.AddField(
            model_name='gptelementary',
            name='level',
            field=models.CharField(default='초등학생', max_length=30),
        ),
        migrations.AddField(
            model_name='gpthigh',
            name='level',
            field=models.CharField(default='고등학생', max_length=30),
        ),
        migrations.AddField(
            model_name='gptmiddle',
            name='level',
            field=models.CharField(default='중학생', max_length=30),
        ),
        migrations.AddField(
            model_name='gptnative',
            name='level',
            field=models.CharField(default='원어민', max_length=30),
        ),
        migrations.AddField(
            model_name='gpttoeic',
            name='level',
            field=models.CharField(default='토익', max_length=30),
        ),
    ]
