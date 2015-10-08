from django.contrib.auth.decorators import login_required


@login_required(login_url='/logearse')
def admin(request):
	return request.user.groups.filter(name__in=['ADMIN']).exists()