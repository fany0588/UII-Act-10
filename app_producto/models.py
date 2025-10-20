from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)
    id_ingrediente = models.PositiveIntegerField() # Asumiendo que id_ingrediente es un entero. Podría ser una ForeignKey si tienes una tabla de Ingredientes.

    def __str__(self):
        return f'Producto: {self.nombre}'