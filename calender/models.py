from django.db import models

# Create your models here.
class Calender(models.Model):
    date = models.DateField(auto_now_add=True)
    reason = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.date}-->{self.reason}'