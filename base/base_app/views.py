from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(reuest):
	return HttpResponse("<h2>#Welcome</h2>")

def index(request):
        return HttpResponse("<h2>#ZOMBIE</h2>")

