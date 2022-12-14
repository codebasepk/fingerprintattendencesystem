# Generated by Django 4.1.3 on 2022-11-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_fingerprintprofilemodel_checkintime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='checkinstatus',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='checkintime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='checkouttime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='currentdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='exitstatus',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='fpid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
