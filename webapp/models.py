from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    mobile_number = models.CharField(max_length =10, blank=False)
    age = models.IntegerField(blank=False)
    education = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20, blank=False)


    def __str__(self):
        return self.first_name