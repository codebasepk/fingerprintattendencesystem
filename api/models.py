from django.db import models


STATE_CHOICE = ((
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('Late', 'Late'),
                ))

LEAVING_CHOICE = ((
    ('AtTime', 'AtTime'),
    ('Early', 'Early'),
    ('OverTime', 'OverTime'),
                ))


class FingerprintProfileModel(models.Model):
    username = models.CharField(max_length=100)
    checkinstatus = models.CharField(max_length=100)
    currentdate = models.DateField(auto_now=False, auto_now_add=False)
    checkintime = models.CharField(max_length=100)
    exitstatus = models.CharField(max_length=100)
    checkouttime = models.CharField(max_length=100, blank=True, null=True, default=None)
    fpid = models.IntegerField()


class RegisterPersonModel(models.Model):
    personName = models.CharField(max_length=100)
    fpid = models.IntegerField(unique=True)
    joiningdatetime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)

