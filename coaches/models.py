from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):

    user = models.OneToOneField(User)

    date_of_birth = models.DateField()

    gender = models.CharField(max_length = 1,
        choices=(('M', 'Male'), ('F', 'Female')), default='M')

    phone = models.CharField(max_length = 24)

    address = models.CharField(max_length = 255)

    skype = models.CharField(max_length = 128)

    description = models.TextField()


    def __unicode__(self):
        return self.user.username
