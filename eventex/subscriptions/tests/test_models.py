# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Henrique Bastos',
			cpf='12345678901',
			email='henrique@bastos.net',
			phone='21-96186180'
		)

	def test_create(self):
		'Subscription must have name,cpf,email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		'Method __unicode__() is not properly set up'
		self.assertEqual(u'Henrique Bastos', unicode(self.obj))

	def test_paid_default_value_is_False(self):
		'By default paid must be False.'
		self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		# Create a first entry to force collision
		Subscription.objects.create(
			name='Henrique Bastos',
			cpf='12345678901',
                        email='henrique@bastos.net',
                        phone='21-96186180'
                )

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(
                        name='Henrique Bastos',
                        cpf='12345678901',
                        email='outro@bastos.net',
                        phone='21-96186180'
                )
		self.assertRaises(IntegrityError, s.save)

	def test_email_can_repeat(self):
                'Email is not unique anymore'
                s = Subscription.objects.create(
                        name='12345 Henrique Bastos',
                        cpf='12345',
                        email='henrique@bastos.net',
                        phone='12345'
                )
		self.assertEqual(2, s.pk)

