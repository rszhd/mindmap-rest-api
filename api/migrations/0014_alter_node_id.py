# Generated by Django 5.1.1 on 2024-10-02 12:19

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_mindmap_id_alter_node_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.CharField(default=uuid.uuid4().hex[:50], editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
