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
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
def subscribe(request):
	if request.method == "POST":
		form = SubscriptionForm(request.POST)
		if form.is_valid():
			obj = Subscription(**form.cleaned_data)
			obj.save()
			return HttpResponseRedirect("/inscricao/%d/" % 1)
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

