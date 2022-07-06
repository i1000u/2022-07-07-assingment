# Generated by Django 4.0.5 on 2022-07-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='today_feeling',
            field=models.CharField(choices=[('HAPPY', 'happy'), ('SAD', 'sad'), ('ANGRY', 'angry'), ('JEALOUS', 'jealous')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(default='천우', max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=b'I00\n'),
        ),
    ]