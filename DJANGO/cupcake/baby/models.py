from django.db import models

# Create your models here.

class Baby(models.Model):
    title = models.CharField(max_length=100)
    is_Emergency = models.BooleanField(default=False)

    def __str__(self):
        return self.title
