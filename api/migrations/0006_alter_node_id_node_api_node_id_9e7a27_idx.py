# Generated by Django 5.1.1 on 2024-09-30 18:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_node_flow_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="node",
            name="id",
            field=models.CharField(
                default=uuid.uuid4().hex[:50],
                editable=False,
                max_length=20,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddIndex(
            model_name="node",
            index=models.Index(fields=["id"], name="api_node_id_9e7a27_idx"),
        ),
    ]
