from django.conf import settings
from django.db import models


# Create your models here.

class MemberData(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    memberNumber = models.CharField(max_length=120)
    expirationDate = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.memberNumber
