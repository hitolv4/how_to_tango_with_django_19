from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	#crea un diccionario para pasar al motor template como su contexto
	# nota que la clave blodmessage es la mismaque {{ bolmessage }}enel template
	context_dict={'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html',context=context_dict)

def rangoindex(request):
	return HttpResponse('<h1>Rango index</h1>')

def about(request):
	return HttpResponse('Rango says here is the about page.')