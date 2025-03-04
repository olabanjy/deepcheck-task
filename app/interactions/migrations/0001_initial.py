# Generated by Django 4.2.13 on 2024-07-04 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LLMInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField(verbose_name='input_data')),
                ('output_data', models.TextField(verbose_name='output_data')),
                ('input_metric', models.TextField(verbose_name='input_metric')),
                ('output_metric', models.TextField(verbose_name='output_metric')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interactions.llminteraction')),
            ],
        ),
    ]
