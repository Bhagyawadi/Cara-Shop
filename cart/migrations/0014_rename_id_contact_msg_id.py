# Generated by Django 5.0.6 on 2025-01-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='id',
            new_name='msg_id',
        ),
    ]
