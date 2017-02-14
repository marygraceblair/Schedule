from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=10)
    number = models.PositiveSmallIntegerField()


class Section(models.Model):
    lettter = models.CharField(max_length=5)
    
