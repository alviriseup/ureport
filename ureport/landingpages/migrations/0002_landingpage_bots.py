# Generated by Django 3.2.8 on 2021-10-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0004_alter_bot_description"),
        ("landingpages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="landingpage",
            name="bots",
            field=models.ManyToManyField(blank=True, to="bots.Bot"),
        ),
    ]
