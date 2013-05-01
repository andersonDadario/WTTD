# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
	name = models.CharField(_("nome"), max_length=100)
	cpf = models.CharField(_("CPF"), max_length=11, unique=True)
	email = models.EmailField(_("email"), unique=True)
	phone = models.CharField(_("telefone"), max_length=20)
	created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
	paid = models.BooleanField(_('Pago'), default=False)

	class Meta:
		ordering = ['created_at']
		verbose_name = _("inscricao")
		verbose_name_plural = _("inscricoes")

	def __unicode__(self):
		return self.name
