from django.db import models
from ckeditor.fields import RichTextField

class Contact_person(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photo/%y/%m/%m')
    description = RichTextField(blank=True,null=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    status = models.BooleanField(default=True)


    def __str__(self):
       return self.name
