# Generated by Django 3.2.6 on 2021-08-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0012_populate_flow_results"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pollwordcloud",
            name="words",
            field=models.JSONField(default=dict),
        ),
    ]
