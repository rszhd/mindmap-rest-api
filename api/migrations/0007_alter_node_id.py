# Generated by Django 5.1.1 on 2024-09-30 18:36

from django.db import migrations, models

import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_node_id_node_api_node_id_9e7a27_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.CharField(default=uuid.uuid4().hex[:50], editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
