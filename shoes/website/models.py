from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    