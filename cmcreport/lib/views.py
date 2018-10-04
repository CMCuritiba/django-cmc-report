# -*- coding: utf-8 -*-

from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View

#----------------------------------------------------------------------------------------
# Classe base para demais classes de relatórios
#----------------------------------------------------------------------------------------
class CMCReportView(PDFTemplateResponseMixin, ContextMixin, View):
	template_name = "relatorio_test.html"	

	def get_context_data(self, **kwargs):
		context = super(PDFTemplateResponseMixin, self).get_context_data(**kwargs)
		context['pagesize'] = 'A4 portrait'
		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		return self.get(request, *args, **kwargs)			