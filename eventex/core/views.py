# coding: utf8
#fuck the versions ...

from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'index.html')

def speaker_detail(request, slug):
	return render(request, 'core/speaker_detail.html')
