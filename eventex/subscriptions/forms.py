# coding: utf-8

#v1
'''
class SubscriptionForm(object):
	pass
'''

#v2
'''
from django import forms
class SubscriptionForm(forms.Form):
        name = forms.CharField()
        cpf = forms.CharField()
        email = forms.EmailField()
        phone = forms.CharField()
'''

#v3
'''
from django import forms
from django.utils.translation import ugettext as _
class SubscriptionForm(forms.Form):
	name = forms.CharField(label=_("Nome"))
	cpf = forms.CharField(label=_("CPF"), max_length=11)
	email = forms.EmailField(label=_("Email"))
	phone = forms.CharField(label=_("Telefone"))
'''

#v4 - Alinhando Form com Model
from django import forms
from eventex.subscriptions.models import Subscription
class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
