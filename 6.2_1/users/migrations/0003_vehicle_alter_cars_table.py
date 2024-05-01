# Generated by Django 5.0.4 on 2024-04-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_cars_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("model", models.CharField(max_length=255)),
                ("price", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "vehicle",
            },
        ),
        migrations.AlterModelTable(
            name="cars",
            table="cars",
        ),
    ]
