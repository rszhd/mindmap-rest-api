# Generated by Django 5.1.1 on 2024-09-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_node_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="mindmap",
            name="flow_data",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
