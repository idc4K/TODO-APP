from django.db import models

class question(models.Model):
    titre = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
# Create your models here.
