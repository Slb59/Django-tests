# Generated by Django 4.2 on 2023-04-26 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0004_band_description_band_sold_band_type_band_year_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="band",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="listings.band",
            ),
        ),
    ]