from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_room_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                (
                    "status",
                    models.CharField(
                        choices=[("on", "on"), ("off", "off")],
                        default="on",
                        max_length=3,
                        unique=True,
                        null=False,
                    ),
                ),
            ],
            options={
                "verbose_name": "Status",
                "verbose_name_plural": "Statuses",
                "db_table": "Statuses",
            },
        ),
    ]
