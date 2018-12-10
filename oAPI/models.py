from django.conf import settings
from django.db import models


# Create your models here.

class MemberData(models.Model):
    firstName = models.CharField(max_length=120, null=True, blank=True)
    lastName = models.CharField(max_length=120, null=True, blank=True)
    memberNumber = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.memberNumber
