from django.shortcuts import render

from .models import Categoria

def index(request):
    latest_question_list = Categoria.objects.order_by('name')[:5]
    context = {'latest_question_list': latest_question_list}
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