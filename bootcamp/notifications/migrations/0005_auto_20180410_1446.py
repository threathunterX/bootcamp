# Generated by Django 2.0.4 on 2018-04-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20180329_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='verb',
            field=models.CharField(choices=[('L', 'liked'), ('C', 'commented'), ('F', 'cavorited'), ('A', 'answered'), ('W', 'accepted'), ('E', 'edited'), ('K', 'also commented'), ('I', 'logged in'), ('O', 'logged out'), ('V', 'voted on'), ('S', 'shared'), ('U', 'created an account')], max_length=1),
        ),
    ]