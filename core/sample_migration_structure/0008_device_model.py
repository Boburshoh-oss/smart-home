from django.db import migrations
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_sensor_model"),
    ]

    operations = [
        migrations.CreateModel(

            name="Device",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, null=False, blank=False)),
                ("description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("channels", models.ManyToManyField(to="core.Channel", null=False)),
                (
                    "home",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="devices",
                        to="core.home",
                        null=False,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="devices",
                        to="core.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="channel",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="channels",
                to="core.room",
                null=False,
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="channels",
                to="core.status",
                null=False,
            ),
        ),
    ]
