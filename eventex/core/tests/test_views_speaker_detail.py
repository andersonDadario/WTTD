# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
	def setUp(self):
		Speaker.objects.create(
			name='Anderson Dadario',
			slug='anderson-dadario',
			url='https://dadario.com.br',
			description='Software Security Consultant'
		)
		url = r('core:speaker_detail', kwargs={'slug': 'anderson-dadario'})
		self.resp = self.client.get(url)

	def test_get(self):
		'GET should result in 200.'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Template should be core/speaker_detail.html.'
		self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

	def test_html(self):
		'Html must contain data.'
		self.assertContains(self.resp, 'Anderson Dadario')
		self.assertContains(self.resp, 'Software Security Consultant')
		self.assertContains(self.resp, 'https://dadario.com.br')

	def test_context(self):
		'Speaker must be in context.'
		speaker = self.resp.context['speaker']
		self.assertIsInstance(speaker, Speaker)

class SpeakerDetailtNotFound(TestCase):
	def test_not_found(self):
		url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
		response = self.client.get(url)
		self.assertEqual(404, response.status_code)
