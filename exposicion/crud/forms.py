from django import forms
from .models import Autor
from .models import Libro

class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro		
