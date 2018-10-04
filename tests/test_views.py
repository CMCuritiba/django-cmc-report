# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory, Client
from unittest.mock import patch, MagicMock, Mock
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.test import TestCase, RequestFactory
from cmcreport.lib.views import CMCReportView

from easy_pdf.views import PDFTemplateView

class CMCReportViewTests(TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_class(self):
		view = CMCReportView()


	def test_report(self):
		response = self.client.get('/test/')
		content = response.content
		self.assertEqual(content[:4], b'%PDF')