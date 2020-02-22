from django.db import models

class Noticia(models.Model):
    titulo = models.CharField('titulo' , max_length=128, blank=True, null=True)
    conteudo = models.TextField()
    autor = models.CharField('autor', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

      
    

# Create your models here.
