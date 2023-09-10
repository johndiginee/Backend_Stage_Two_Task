from django.db import models

class Person(models.Model):
    """Represent a person data.
    
    Attributes:
        name: The person full name.
    """
    name = models.CharField(max_length=255)