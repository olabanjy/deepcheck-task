# Generated by Django 4.2.13 on 2024-07-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LLMFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
