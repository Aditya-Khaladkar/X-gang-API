from django.db import models

# Create your models here.
class xgang(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    choice = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))
    chutyap = models.CharField(choices=choice, max_length=1)
    githubLink = models.CharField(max_length=50)