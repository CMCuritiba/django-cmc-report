# coding=utf-8

from django.urls import include, path

from easy_pdf.views import PDFTemplateView
from .views import ViewCMCReport

urlpatterns = [
    path('test/', ViewCMCReport.as_view(), name='test'),
    #url(r'^simple/$', PDFTemplateView.as_view(template_name='simple.html')),
    #url(r'^user/(?P<pk>\d+)/$', PDFUserDetailView.as_view()),
]