# Generated by Django 4.1.3 on 2022-11-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_fingerprintprofilemodel_checkouttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='checkintime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='currentdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='exitstatus',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='fpid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
