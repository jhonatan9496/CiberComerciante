from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import*
# Create your views here.
def autor_view(request, title):
	autor = get_object_or_404(Autor, nombre=title)
	return render(request, 'autor.html',{'autor':autor})

def libro_view(request, title):
	libro = get_object_or_404(Libro, titulo=title)
	return render(request, 'libro.html',{'libro':libro})	