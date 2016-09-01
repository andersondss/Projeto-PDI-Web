# *coding: utf-8*
import sys
import os
import django

# import django.core.handlers.wsgi

sys.path.append("/home/bas/app_d63ebec2-0a76-4a0a-86e8-67377cccbdf8")
os.environ['DJANGO_SETTINGS_MODULE'] = 'projeto_pdi_web.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-egg'

# application = django.core.handlers.wsgi.WSGIHandler()
