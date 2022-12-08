from django.shortcuts import render

# Create your views here.

def hello_world(request):
	render(request, 'hello_world.html', {})
