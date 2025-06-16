from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=255, blank=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    usuario_asignado = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_limite = models.DateField()

    def __str__(self):
        return self.titulo

class Venta(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('cerrada', 'Cerrada'),
        ('cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.producto} - {self.cliente.nombre}"
