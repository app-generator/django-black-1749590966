# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Tool(models.Model):

    #__Tool_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    command = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    #__Tool_FIELDS__END

    class Meta:
        verbose_name        = _("Tool")
        verbose_name_plural = _("Tool")



#__MODELS__END
