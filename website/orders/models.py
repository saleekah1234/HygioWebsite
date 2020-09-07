from django.db import models


class Order(models.Model):
    name=models.TextField(max_length=50)
    #phone=models.PhoneField(blank=True, help_text='Contact phone number')
    item=models.TextField(max_length=50)
    





# Create your models here.
