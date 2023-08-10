from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=15, unique=True, null=False)
    speed = models.CharField(max_length=20, null=True)
    pop_name = models.CharField(max_length=50, null=True)
    dslam_hostname = models.CharField(max_length=50, null=True)
    frame = models.IntegerField(null=True)
    attainable_speed = models.IntegerField(null=True)

    def __str__(self):
        return self.name + ' ' + self.phone
