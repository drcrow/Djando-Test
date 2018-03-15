from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria_id 	= models.AutoField(primary_key=True)
    nombre 			= models.CharField(max_length=30)
    descripcion 	= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
##############################################################################################################################
class Producto(models.Model):
    MATERIALES = (
        ('Pl', 'Plastico'),
        ('Ma', 'Madera'),
        ('Cr', 'Cristal'),
        ('Cu', 'Cuero'),
    )
    COLORES = (
        ('N', 'Negro'),
        ('B', 'Blanco'),
        ('R', 'Rojo'),
        ('V', 'Verde'),
        ('A', 'Azul'),
    )

    producto_id 	= models.AutoField(primary_key=True)
    categoria_id 	= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre 			= models.CharField(max_length=30)
    descripcion 	= models.CharField(max_length=100)
    precio	 		= models.FloatField(default=0)
    stock			= models.IntegerField(default=0)
    material		= models.CharField(max_length=2, choices=MATERIALES)
    color 			= models.CharField(max_length=1, choices=COLORES)
    largo			= models.IntegerField(default=0)
    ancho 			= models.IntegerField(default=0)
    alto 			= models.IntegerField(default=0)

    def __str__(self):
        return self.nombre+" ("+str(self.stock)+")"
##############################################################################################################################
#class DescripcionProducto(models.Model):
#    producto_desc_id 	= models.AutoField(primary_key=True)
#    producto_id 		= models.ForeignKey(Producto, on_delete=models.CASCADE)
#    descripcion 		= models.CharField(max_length=100)
#    nombre 				= models.CharField(max_length=30)
#    precio	 			= models.FloatField(default=0)
#
#    def __str__(self):
#        return self.nombre
##############################################################################################################################
class Compra(models.Model):
    CIUDADES = (
        ('CB', 'Cordoba'),
        ('CP', 'Carlos Paz'),
        ('VM', 'Villa Maria'),
        ('RT', 'Rio Tercero'),
        ('RC', 'Rio Cuarto'),
    )

    compra_id 		= models.AutoField(primary_key=True)
    usuario_id 		= models.ForeignKey(User, on_delete=models.CASCADE)#funcionará esto con los usuarios por defecto o debo crear mi propia tabla?
    fecha			= models.DateTimeField(auto_now=True, auto_now_add=False)
    total			= models.FloatField(default=0)
    direccion		= models.CharField(max_length=100)
    departamento 	= models.CharField(max_length=10)
    ciudad			= models.CharField(max_length=2, choices=CIUDADES)
    telefono		= models.CharField(max_length=20)
    estado			= models.CharField(max_length=100)#no estoy seguro de si es el "estado" de la compra o el "estado" de la "ciudad"

    def __str__(self):
        return self.fecha+" ($"+self.total+")"
##############################################################################################################################
class DetalleCompra(models.Model):
    detalle_id 			= models.AutoField(primary_key=True)
#    producto_desc_id 	= models.ForeignKey(DescripcionProducto, on_delete=models.CASCADE)
    producto_id		 	= models.ForeignKey(Producto, on_delete=models.CASCADE)
    compra_id 			= models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad			= models.IntegerField(default=0)
    subtotal			= models.FloatField(default=0)

    def __str__(self):
        return self.producto_id+" ($"+self.subtotal+")"
##############################################################################################################################