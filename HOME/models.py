from django.db import models

# Create your models here.


class Categorias(models.Model):
    descripcion = models.CharField(max_length=10)    
    def __str__(self):
        return self.descripcion

class Productos(models.Model):
    titulo = models.CharField(max_length=64)
    imagen = models.ImageField(upload_to='HOME', null=True, blank=True)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='categoria')
    def __str__(self):
        return f"Producto: #{self.id} Titulo:{self.titulo}, Imagen: {self.imagen} ; Descripcion: {self.descripcion}; Precio: {self.precio}; Categoria: {self.categoria}"
