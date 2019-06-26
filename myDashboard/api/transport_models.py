from django.db import models

class UniData(models.Model):
    Promo = models.TextField()

    def __str__(self):
        return ''