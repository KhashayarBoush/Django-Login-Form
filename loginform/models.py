from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 300)

    def __str__(self):
        return self.email
