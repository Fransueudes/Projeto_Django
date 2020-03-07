from django.contrib import admin
from .models import Noticia
from .models import Pessoa
from .models import Tag
from .models import Comentario

@admin.register(Noticia, Pessoa, Tag, Comentario)


class NoticiaAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class PessoaAdmin(admin.ModelAdmin):
    pass

class ComentarioAdmin(admin.ModelAdmin):
    pass


# Register your models here.
