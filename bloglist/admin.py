from django.contrib import admin
from .models import Post
from .models import Categoria

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('categoria', 'status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Categoria)
class CatAdmin(admin.ModelAdmin):
    list_display = ('descrizione', )
    list_filter = ('descrizione', )
    

    


