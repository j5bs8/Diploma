# Generated by Django 4.1.3 on 2022-11-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_memory_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memory_freq",
            name="freq",
            field=models.SmallIntegerField(verbose_name="Частота"),
        ),
    ]
