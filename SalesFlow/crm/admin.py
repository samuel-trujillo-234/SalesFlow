from django.contrib import admin
from .models import Cliente, Tarea, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'empresa')
    search_fields = ('nombre', 'email', 'empresa')
    list_filter = ('empresa',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario_asignado', 'cliente', 'estado', 'fecha_limite')
    search_fields = ('titulo', 'descripcion', 'cliente__nombre')
    list_filter = ('estado', 'usuario_asignado', 'fecha_limite')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cliente', 'valor', 'fecha', 'estado')
    search_fields = ('producto', 'cliente__nombre')
    list_filter = ('estado', 'fecha')
