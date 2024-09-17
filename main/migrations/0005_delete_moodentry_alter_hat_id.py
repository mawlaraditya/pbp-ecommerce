# Generated by Django 5.1.1 on 2024-09-17 15:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_hat_price_alter_moodentry_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MoodEntry',
        ),
        migrations.AlterField(
            model_name='hat',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
