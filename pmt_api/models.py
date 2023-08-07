from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    speed = models.CharField(max_length=20)
    pop_name = models.CharField(max_length=50)
    dslam_hostname = models.CharField(max_length=50)
    frame = models.IntegerField()
    attainable_speed = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.phone
