# Generated by Django 2.2.20 on 2021-07-28 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0001_initial"),
        ("polls", "0064_deduplicate_pollresponsecategories"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="pollresponsecategory",
            unique_together={("question", "flow_result_category"), ("question", "rule_uuid")},
        ),
    ]
