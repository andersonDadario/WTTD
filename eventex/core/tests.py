# coding: utf8

#v1
'''
from django.test import TestCase
class HomepageTest(TestCase):
	def test_get(self):
		'GET / must return status code 200.'
		response = self.client.get('/')
		self.assertEqual(200, response.status_code)
		self.assertTemplateUsed(response, 'index.html')
'''

#v2
from django.test import TestCase
class HomepageTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/')

	def test_get(self):
		'GET / must return status code 200.'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Homepage must use template index.html.'
		self.assertTemplateUsed(self.resp, 'index.html')

	def tearDown(self):
		pass
