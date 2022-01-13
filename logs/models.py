from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models

class LogBook(models.Model):
    owner       = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='logbooks', on_delete=models.CASCADE)
    name        = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Log(models.Model):
    MODE_CHOICES = (
        ("PSK31", "PSK31"),
        ("DSTAR", "DSTAR"),
        ("SSTV", "SSTV"),
        ("RTTY", "RTTY"),
        ("SSB", "SSB"),
        ("USB", "USB"),
        ("LSB", "LSB"),
        ("FT8", "FT8"),
        ("AM", "AM"),
        ("FM", "FM"),
        ("CW", "CW"),
    )

    mode            = models.CharField(max_length=10, choices=MODE_CHOICES, blank=False, null=False)
    date            = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    frequency       = models.FloatField(default=0000.00, blank=False, null=False)
    time            = models.TimeField(auto_now_add=True, blank=False, null=False)
    callsign        = models.CharField(max_length=10, blank=False, null=False)
    band            = models.FloatField(blank=False, null=False)

    report_received = models.IntegerField(validators=[MaxValueValidator(599), MinValueValidator(111)], blank=True, null=True)
    report_send     = models.IntegerField(validators=[MaxValueValidator(599), MinValueValidator(111)], blank=True, null=True)
    comments        = models.TextField(blank=True, null=True)
    favorite        = models.BooleanField(default=False)

    book            = models.ForeignKey(LogBook, related_name='logs', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.callsign
