from django.db import models
class Students(models.Model):
    name = models.CharField()
    age = models.CharField()
    cgpa = models.CharField()
    def __str__(self):
        return self.name
