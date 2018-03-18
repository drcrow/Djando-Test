"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from productos.models import Categoria, Compra, DetalleCompra, Producto




# USERS API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model 	= User
        fields 	= ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset 			= User.objects.all()
    serializer_class 	= UserSerializer

# CATEGORIAS API
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model 	= Categoria
        fields 	= ('categoria_id', 'nombre', 'descripcion')

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset 			= Categoria.objects.all()
    serializer_class 	= CategoriaSerializer

# COMPRAS API
class CompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model 	= Compra
        fields 	= ('fecha', 'total', 'usuario_id', 'direccion')

class CompraViewSet(viewsets.ModelViewSet):
    queryset 			= Compra.objects.all()
    serializer_class 	= CompraSerializer

# DETALLE COMPRAS API
class DetalleComprasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model 	= DetalleCompra
        fields 	= ('producto_id', 'cantidad', 'subtotal')

class DetalleComprasViewSet(viewsets.ModelViewSet):
    queryset 			= DetalleCompra.objects.all()
    serializer_class 	= DetalleComprasSerializer

# PRODUCTOS API
class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model 	= Producto
        fields 	= ('nombre', 'descripcion', 'precio')

class ProductosViewSet(viewsets.ModelViewSet):
    queryset 			= Producto.objects.all()
    serializer_class 	= ProductosSerializer




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', 			UserViewSet)
router.register(r'api/categorias', 		CategoriaViewSet)
router.register(r'api/compras', 		CompraViewSet)
router.register(r'api/detallecompras', 	DetalleComprasViewSet)
router.register(r'api/productos', 		ProductosViewSet)

urlpatterns = [
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


