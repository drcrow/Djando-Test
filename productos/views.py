from django.shortcuts import render
from .models import Categoria, Producto, Compra, DetalleCompra
import json

def index(request):

	if request.POST:
		#compra_form = request.POST
		#context 	= {'compra_form': compra_form}

		#user_id = request.POST.get("userid", "")
		user = request.user
		date = request.POST.get("date", "")
		city = request.POST.get("city", "")
		addr = request.POST.get("addr", "")
		apt = request.POST.get("apt", "")
		tel = request.POST.get("tel", "")
		#timezone.now()
		compra = Compra(usuario_id=user, fecha=date, ciudad=city, direccion=addr, departamento=apt, telefono=tel)
		compra.save()

		prods = json.loads(request.POST.get("productos", ""))

		for p_id, p_cant in prods.items():
			prod = Producto.objects.get(producto_id=p_id)
			compraDet = DetalleCompra(producto_id=prod, compra_id=compra, cantidad=p_cant, subtotal=(float(prod.precio) * float(p_cant)))
			compraDet.save()

		context 	= {'compra': compra, 'prods': prods}
		return render(request, 'productos/abc.html', context)
	else:
		usuario 	= request.user
		productos 	= Producto.objects.order_by('nombre')
		ciudades 	= Compra.CIUDADES
		context 	= {'productos': productos, 'ciudades': ciudades}
		return render(request, 'productos/abc.html', context)

# Create your views here.
#def index(request):
#    return HttpResponse("Hola!! Este es el index de PRODUCTOS")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id) 

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)