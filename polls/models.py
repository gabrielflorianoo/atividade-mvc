from django.db import models

# Create your models here.
class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # Nome do animal
    species = models.CharField(max_length=100)           # Espécie do animal
    emoji = models.CharField(max_length=2)               # Emoji representando o animal
    description = models.TextField(blank=True, null=True)  # Descrição opcional do animal
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do registro

    def __str__(self):
        return f"{self.emoji} {self.name} ({self.species})"