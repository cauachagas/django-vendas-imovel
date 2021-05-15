from django.contrib import admin

# Register your models here.
from app.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "data_cadastro")
