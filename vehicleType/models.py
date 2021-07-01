from django.db import models

class Vehicle_type(models.Model):
    type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.type_name