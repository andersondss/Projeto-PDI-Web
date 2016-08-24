#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Codification(models.Model):

    image = models.ImageField(upload_to="upload/codification/", verbose_name="Imagem", blank=False)
    description = models.CharField("Descrição", max_length=50, blank=True)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = "Codificação"
        verbose_name_plural = "Codificações"
        ordering = ["created_at"]
