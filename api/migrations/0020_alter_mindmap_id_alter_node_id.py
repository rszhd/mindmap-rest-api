# Generated by Django 5.1.1 on 2024-10-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_node_note_alter_node_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mindmap',
            name='id',
            field=models.CharField(editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.CharField(editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
