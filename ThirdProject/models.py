from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)  # Adjust length as needed
    place = models.CharField(max_length=255)

    def _str_(self):
        return self.name