from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def is_member(user):
	return user.is_superuser or user.groups.filter(name='Member').exists()

@user_passes_test(is_member)
def index(request):
	return render(request, "index.html")
	
