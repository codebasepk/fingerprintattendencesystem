# Generated by Django 4.1.3 on 2022-11-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_fingerprintprofilemodel_currentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='currentdate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
