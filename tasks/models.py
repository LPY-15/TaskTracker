from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=30, default='unknown')
    last_name = models.CharField(max_length=30, default='unknown')
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name