from django.shortcuts import render
from .forms import*
# Create your views here.
def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()
	return render(request, 'signup.html', {'form':form})
