import os

import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
from django.shortcuts import render, redirect
from django.conf import settings

from projeto_pdi_web.core.models import Codification, Segmentation
from projeto_pdi_web.core.forms import FormCodification, FormSegmentation
from projeto_pdi_web.common.lib_codification import run_orb
from projeto_pdi_web.common.lib_segmentation import segmentation_slic


def home(request):
    return render(request, "home.html")


def codification(request):

    template_name = "codificacao.html"
    context = {}
    if request.method == "POST":
        form = FormCodification(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            codification = Codification.objects.all().order_by('-id')[0]
            img = cv2.imread("{0}/{1}".format(settings.MEDIA_ROOT, codification.image.name))
            # print type(img)
            # print img.shape
            # plt.imshow(img, cmap='gray')
            # plt.show()
            kp, descriptors, img_keypoints = run_orb(img)
            # plt.imshow(img_keypoints, cmap='gray')
            # plt.show()
            print "{0}/{1}".format(settings.MEDIA_ROOT, "upload/codification/output/img.png")
            cv2.imwrite("{0}/{1}".format(settings.MEDIA_ROOT, "upload/codification/output/img.png"),
                        img_keypoints)
            # context["keypoints"] = kp
            # context["descriptors"] = descriptors
            print codification.image
            context["image"] = codification.image
            context["image_cod"] = "media/upload/codification/output/img.png"
            return render(request, "codificacao_sucesso.html", context)
    else:
        form = FormCodification()

    context["form"] = form
    return render(request, template_name, context)


def similarity(request):
    return render(request, "similariedade.html")


def segmentation(request):

    template_name = "segmentacao.html"
    context = {}
    if request.method == "POST":
        form = FormSegmentation(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            segmentation = Segmentation.objects.all().order_by('-id')[0]
            img = cv2.imread("{0}/{1}".format(settings.MEDIA_ROOT, codification.image.name))
            kp, descriptors, img_keypoints = run_slic(img)
            # plt.imshow(img_keypoints, cmap='gray')
            # plt.show()
            print "{0}/{1}".format(settings.MEDIA_ROOT, "upload/codification/output/img.png")
            cv2.imwrite("{0}/{1}".format(settings.MEDIA_ROOT, "upload/codification/output/img.png"),
                        img_keypoints)
            # context["keypoints"] = kp
            # context["descriptors"] = descriptors
            print codification.image
            context["image"] = codification.image
            context["image_cod"] = "media/upload/codification/output/img.png"
            return render(request, "codificacao_sucesso.html", context)
    else:
        form = FormCodification()

    context["form"] = form
    return render(request, template_name, context)
