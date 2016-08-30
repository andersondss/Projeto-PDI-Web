#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Codification(models.Model):

    image = models.ImageField(upload_to="upload/codification/input/", verbose_name="Imagem", blank=False)
    image_cod = models.ImageField(upload_to="upload/codification/output/", verbose_name="Imagem", blank=True)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = "Codificação"
        verbose_name_plural = "Codificações"
        ordering = ["created_at"]


class Segmentation(models.Model):

    concept_choice = (
        (0, "Gato"),
        (1, "Cavalo"),
        (2, "Avião")
    )
    concept = models.IntegerField("Conceito", choices=concept_choice, default=0, blank=False)
    image = models.ImageField(upload_to="upload/segmentation/input/", verbose_name="Imagem", blank=False)
    # description = models.CharField("Descrição", max_length=50, blank=True)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = "Segmentação"
        verbose_name_plural = "Segmentações"
        ordering = ["created_at"]


class ShapeSimilarity(models.Model):

    first_image = models.ImageField(upload_to="upload/similarity/input/", verbose_name="Primeira Imagem", blank=False)
    second_image = models.ImageField(upload_to="upload/similarity/input/", verbose_name="Segunda Imagem", blank=False)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = "Similaridade"
        verbose_name_plural = "Similaridades"
        ordering = ["created_at"]
