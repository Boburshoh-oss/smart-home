from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_channel_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, null=False, blank=False)),
                ("description", models.TextField(blank=True)),
                ("num_of_channels", models.IntegerField(choices=[(1, "1"), (4, "4")], null=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
