from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('projeto_pdi_web.core.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^codificacao-cena$', 'codification', name='codification'),
                       url(r'^similariedade-formas$', 'similarity', name='similarity'),
                       url(r'^segmentacao$', 'segmentation', name='segmentation'),
                       )
