from django.db import models

# Create your models here.

class Nomes(models.Model):
    nome = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nome