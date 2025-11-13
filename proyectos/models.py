from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    creador = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    monto_requerido = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=50, default='En revisión')

    def __str__(self):
        return self.nombre