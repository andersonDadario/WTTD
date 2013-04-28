# coding: utf-8

#v1
'''
from django.shortcuts import render
def subscribe(request):
	return render(request, 'subscriptions/subscription_form.html') 
'''

#v2
'''
from django.shortcuts import render
def subscribe(request):
	return render(request,
		'subscriptions/subscription_form.html', 
		{'form': None}
	)
'''

#v3
'''
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
def subscribe(request):
	return render(request,
		'subscriptions/subscription_form.html', 
                {'form': SubscriptionForm()}
	)
'''

#v4
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
def subscribe(request):
	if request.method == "POST":
		form = SubscriptionForm(request.POST)
		if form.is_valid():
			# Antes
			# obj = Subscription(**form.cleaned_data)
			# obj.save()
			obj = form.save()
			return HttpResponseRedirect("/inscricao/%d/" % obj.pk)
		else:
			return render(request,
				'subscriptions/subscription_form.html',
				{'form':form}
			)
	else:
        	return render(request,
                	'subscriptions/subscription_form.html',
                	{'form': SubscriptionForm()}
        	)
'''

#v5
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	return render(request,
                'subscriptions/subscription_form.html',
                {'form': SubscriptionForm()}
        )

def create(request):
	form = SubscriptionForm(request.POST)
	if not form.is_valid():
                return render(request,
                         'subscriptions/subscription_form.html',
                         {'form':form}
                )

	obj = form.save()
	return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

