from django.db import models

# Crea un modelo simple para asegurar que se genere la migración inicial
class PruebaConexion(models.Model):
    nombre = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Pruebas de Conexión"