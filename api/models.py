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
    username = models.CharField(max_length=100, default=None)
    checkinstatus = models.CharField(max_length=100, default=None)
    currentdate = models.DateField(auto_now=False, auto_now_add=False, blank=False, default=None)
    checkintime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, default=None)
    exitstatus = models.CharField(max_length=100, default=None)
    checkouttime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, default=None)
    fpid = models.IntegerField(default=None)


class RegisterPersonModel(models.Model):
    personName = models.CharField(max_length=100)
    fpid = models.IntegerField(unique=True)
    joiningdatetime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)

