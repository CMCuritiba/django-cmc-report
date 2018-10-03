# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class AutenticaConfig(AppConfig):
    name = 'django-cmc-report.cmcreport'
    verbose_name = "Bibliotec Utilitária de Relatórios"

    def ready(self):
        pass
