# Generated by Django 4.2 on 2023-11-04 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logmaneapp', '0004_alter_athlete_athlete_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_records',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logmaneapp.event'),
        ),
    ]