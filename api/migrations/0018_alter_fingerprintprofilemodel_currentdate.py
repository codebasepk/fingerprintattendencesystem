# Generated by Django 4.1.3 on 2022-11-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_fingerprintprofilemodel_checkouttime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='currentdate',
            field=models.DateField(),
        ),
    ]
