from django.db import models
from django.db import models


# Create your models here.
class MemberRecord(models.Model):
    uid = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.UID

class Record(models.Model):
    student = models.ForeignKey(
        MemberRecord, on_delete=models.CASCADE)  # to be edited
    venue = models.CharField(max_length=10)
    datetime = models.DateTimeField()
# Create your models here.

class VenueRecord(models.Model):
    venue_code=models.CharField(max_length=20)
    location=models.CharField(max_length=150)
    type=models.CharField(max_length=2)
    capacity=models.IntegerField()
