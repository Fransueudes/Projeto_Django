from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome' , max_length=128)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15, 
                                        help_text='Número de telefone celular no formato (99) 99999-9999' )
    telefone_fixo = models.CharField('Telefone fixo', max_length=14, 
                                    help_text='Número de telefone fixo no formato (99) 9999-9999')
    email = models.EmailField('E-mail', blank=True, null=True)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    
    def __str__(self):
        return self.nome


class Noticia(models.Model):
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField('titulo' , max_length=128, blank=True, null=True)
    conteudo = models.TextField()
    autor = models.CharField('autor', max_length=128, blank=True, null=True)
    data = models.DateField('data', max_length=128, blank=True, null=True)
    tags = models.CharField('tag', max_length=128, blank=True, null=True)
      
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

class Comentario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Autor')
    datahora = models.DateField('data', max_length=128, blank=True, null=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, blank=True, null=True)
    comentario = models.TextField()
    
    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

'''class Categoria(models.Model):
    titulo = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')'''

      
    

# Create your models here.
