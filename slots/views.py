from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return HttpResponse('home.html')

@login_required
def security_page(request):
    return HttpResponse('security')
