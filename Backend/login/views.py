from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello")

# Create your views here.
