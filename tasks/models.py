from django.db import models

class task(models.Model):
    task_name = models.CharField(max_length=500)

    def __str__(self):
        return self.task_name