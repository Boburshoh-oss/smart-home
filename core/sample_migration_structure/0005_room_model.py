from django.db import migrations
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_product_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Enter a name for this room", max_length=200, null=False, blank=False
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Enter a description for this room", max_length=1000
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "home_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="core.home",
                        null=False,
                    ),
                ),
            ],
        ),
    ]
