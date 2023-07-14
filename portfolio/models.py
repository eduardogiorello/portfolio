from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    subtitulo = CharField(max_length=100, null=True)
    description = CharField(max_length=250)
    cliente = CharField(max_length=100, null=True)
    categoria = CharField(max_length=100, null=True)
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)
    

    def __str__(self):
        return 'Proyecto ' + str(self.title) + ' - Cliente - ' + str(self.cliente)