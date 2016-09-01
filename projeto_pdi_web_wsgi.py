# *coding: utf-8*
import sys
import os

sys.path.append("/home/bas/app_d63ebec2-0a76-4a0a-86e8-67377cccbdf8")
sys.path.append("/home/bas/app_e7a18983-405e-4ada-ac68-2738f2767461")
os.environ['DJANGO_SETTINGS_MODULE'] = 'cc_django.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-egg'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()