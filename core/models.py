from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelMultipleChoiceField
from django.conf import settings

JOB_CHOICES = [
    ('LOGISTICS', 'Λογιστικά'),
    ('DOCS', 'Φοροτεχνικά'),
    ('OUT', 'Υπηρεσίες'),
]



class Clientele(models.Model):
    Aa = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ClientModel(models.Model):
    Aa = models.AutoField(primary_key=True, unique=True)
    name = models.ForeignKey(Clientele, on_delete=models.CASCADE)

    time_spent = models.TimeField(default=None)
    belongs_to = settings.AUTH_USER_MODEL
    dec_name = models.CharField(max_length=100, default=None)
    reason = models.CharField(max_length=200, choices=JOB_CHOICES)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dec_name