#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Codification(models.Model):

    image = models.ImageField(upload_to="upload/codification/input/", verbose_name="Imagem", blank=False)
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
        (1, "Avião"),
        (2, "Relógio"),
        (3, "Moto"),
        (4, "Carro"),
        (5, "Cadeira"),
        (6, "Cavalo"),
        (7, "Gavião"),
        (8, "Barco"),
        (9, "Vaca"),
    )

    concept = models.IntegerField("Conceito", choices=concept_choice, default=0, blank=False)
    image = models.ImageField(upload_to="upload/segmentation/input/", verbose_name="Imagem", blank=False)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = "Segmentação"
        verbose_name_plural = "Segmentações"
        ordering = ["created_at"]


class ShapeSimilarity(models.Model):

    first_image = models.ImageField(upload_to="upload/similarity/shape/input/", verbose_name="Primeira Imagem",
                                    blank=False)
    second_image = models.ImageField(upload_to="upload/similarity/shape/input/", verbose_name="Segunda Imagem",
                                     blank=False)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = "Similaridade"
        verbose_name_plural = "Similaridades"
        ordering = ["created_at"]
