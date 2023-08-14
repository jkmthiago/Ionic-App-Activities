from django.contrib import admin
from filmes.models import Movie, Ator

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("nome",)
    list_display = ("nome",)

@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    search_fields = ("nome",)
    list_display = ("nome", "idade", "created_date")
    list_editable = ("idade",)
    