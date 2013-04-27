# coding: utf8

# v1
'''
from django.http import HttpResponse
def homepage(request):
	return HttpResponse('Bem vindo ao EventeX')
'''

# v2
'''
from django.http import HttpResponse
from django.template import loader, Context
def homepage(request):
	t = loader.get_template('index.html')
	c = Context()

	content = t.render(c)

	return HttpResponse(content)
'''

# v3
'''
from django.shortcuts import render_to_response
def homepage(request):
	return render_to_response('index.html')	
'''

# v4
'''
from django.shortcuts import render_to_response
from django.conf import settings
def homepage(request):
	context = {'STATIC_URL': settings.STATIC_URL}
	return render_to_response('index.html', context)
'''

# v5
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
def homepage(request):
	context = RequestContext(request)
	return render_to_response('index.html',context)
'''

# v6
from django.shortcuts import render
def homepage(request):
	return render(request, 'index.html')
