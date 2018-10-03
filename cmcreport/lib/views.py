# -*- coding: utf-8 -*-

from easy_pdf.views import PDFTemplateView

#----------------------------------------------------------------------------------------
# Classe base para demais classes de relatórios
#----------------------------------------------------------------------------------------
class CMCReportView(PDFTemplateView):

	def get_context_data(self, **kwargs):
		context = super(PDFTemplateView, self).get_context_data(**kwargs)
		context['pagesize'] = 'A4 portrait'
		return context

	def get(self, request, *args, **kwargs):
		context = super(PDFTemplateView, self).get_context_data(**kwargs)
		return super(RelatorioVotacao, self).get(request, *args, **kwargs)	

	def post(self, request, *args, **kwargs):
		context = super(PDFTemplateView, self).get_context_data(**kwargs)
		return super(RelatorioVotacao, self).get(request, *args, **kwargs)			