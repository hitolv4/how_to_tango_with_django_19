from django.http import HttpResponse

def index(request):
	return HttpResponse('Rango says hey there partner')

def rangoindex(request):
	return HttpResponse('<h1>Rango index</h1>')

def about(request):
	return HttpResponse('Rango says here is the about page.')