from django.db import models


class Digimon(models.Model):
    name=models.CharField(max_length=255)
    img=models.CharField(max_length=255)
    level=models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.img