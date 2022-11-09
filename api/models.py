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
    dt = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    status = models.CharField(choices=STATE_CHOICE, max_length=50, blank=False)
    picture = models.ImageField(upload_to='pImages', blank=True)
    ldt = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, default=False)
    lstatus = models.CharField(choices=LEAVING_CHOICE, max_length=50, default=False)
