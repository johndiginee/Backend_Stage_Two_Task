from django.db import models

class Person(models.Model):
    """Represent a person data.
    
    Attributes:
        name: The person full name.
        phone_number: The person's phone number.
        email: The person's phone number.
        gender: The person's gender
    """
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField()