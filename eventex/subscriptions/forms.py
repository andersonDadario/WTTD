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
'''
from django import forms
from eventex.subscriptions.models import Subscription
class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		exclude = ('paid',)
'''

#v5 - Validar CPF
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from eventex.subscriptions.models import Subscription

def CPFValidator(value):
	if not value.isdigit():
		raise ValidationError(_(u'CPF deve conter apenas números'))

	if len(value) != 11:
		raise ValidationError(_(u'CPF deve ter 11 algarismos'))

class PhoneWidget(forms.MultiWidget):
	def __init__(self, attrs=None):
		widgets = (
			forms.TextInput(attrs=attrs),
			forms.TextInput(attrs=attrs)
		)
		super(PhoneWidget, self).__init__(widgets, attrs)

	def decompress(self, value):
		if not value:
			return [None, None]

		return value.split('-')

class PhoneField(forms.MultiValueField):
	widget = PhoneWidget

	def __init__(self, *args, **kwargs):
		fields = (
			forms.IntegerField(),
			forms.IntegerField()
		)

		super(PhoneField, self).__init__(fields, *args, **kwargs)

	def compress(self, data_list):
		if not data_list:
			return ''

		if data_list[0] in EMPTY_VALUES:
			raise form.ValidationError(_(u'DDD inválido'))

		if data_list[1] in EMPTY_VALUES:
			raise form.ValidationError(_(u'Número inválido'))

		return '%s-%s' % tuple(data_list)

class SubscriptionForm(forms.ModelForm):
	phone = PhoneField(label=_('Telefone'), required=False)

        class Meta:
                model = Subscription
		#fields = ('name','cpf','email','phone',)
                exclude = ('paid',)

	def __init__(self, *args, **kwargs):
		super(SubscriptionForm, self).__init__(*args, **kwargs)
		self.fields['cpf'].validators.append(CPFValidator)

	def clean_name(self):
		name = self.cleaned_data['name']
		words = map(lambda w: w.capitalize(), name.split())
		capitalized_name = ' '.join(words)
		return capitalized_name

	def clean(self):
		super(SubscriptionForm, self).clean()
		if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
			raise ValidationError(_(u'Informe seu email ou telefone'))
	
		return self.cleaned_data
