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
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
def subscribe(request):
	return render(request,
		'subscriptions/subscription_form.html', 
                {'form': SubscriptionForm()}
	)

