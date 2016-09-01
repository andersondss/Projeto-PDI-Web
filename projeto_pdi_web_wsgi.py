# *coding: utf-8*
import sys
import os

sys.path.append("/home/bas/app_d63ebec2-0a76-4a0a-86e8-67377cccbdf8")
os.environ['DJANGO_SETTINGS_MODULE'] = 'cc_django.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-egg'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()