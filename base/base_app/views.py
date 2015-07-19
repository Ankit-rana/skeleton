from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def home(request):
	template = loader.get_template('base_app/home.html')
	return HttpResponse(template)

def index(request):
        return HttpResponse("<h2>#ZOMBIE</h2>")

