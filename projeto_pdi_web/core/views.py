import os

import cv2
import Image
import numpy as np
from matplotlib import pyplot as plt
from django.shortcuts import render, redirect
from django.conf import settings
import matplotlib.image as mpimg
import scipy.misc

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
            kp, descriptors, img_keypoints = run_orb(img)
            print "{0}/{1}".format(settings.MEDIA_ROOT, "upload/codification/output/img.png")
            cv2.imwrite("{0}/{1}".format(settings.MEDIA_ROOT, "upload/codification/output/img.png"),
                        img_keypoints)
            context["image"] = codification.image
            context["keypoints"] = kp
            context["descriptors"] = descriptors
            context["image_cod"] = "media/upload/codification/output/img.png"
            return render(request, "codificacao_sucesso.html", context)
    else:
        form = FormCodification()

    context["form"] = form
    return render(request, template_name, context)


def segmentation(request):

    template_name = "segmentacao.html"
    context = {}
    if request.method == "POST":
        form = FormSegmentation(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            segmentation = Segmentation.objects.all().order_by('-id')[0]
            concept = segmentation.concept_choice[segmentation.concept][1]
            n_concept = segmentation.concept_choice[segmentation.concept][0]
            img = mpimg.imread("{0}/{1}".format(settings.MEDIA_ROOT, segmentation.image.name))
            img_superpixels, img_mask, img_seg = segmentation_slic(img, n_concept)
            scipy.misc.imsave("{0}/{1}".format(settings.MEDIA_ROOT, "upload/segmentation/output/img_super.png"),
                              img_superpixels)
            scipy.misc.imsave("{0}/{1}".format(settings.MEDIA_ROOT, "upload/segmentation/output/img_mask.png"),
                              img_mask)
            scipy.misc.imsave("{0}/{1}".format(settings.MEDIA_ROOT, "upload/segmentation/output/img_seg.png"),
                              img_seg)
            context["concept"] = concept
            context["image"] = segmentation.image
            context["img_superpixels"] = "media/upload/segmentation/output/img_super.png"
            context["img_mask"] = "media/upload/segmentation/output/img_mask.png"
            context["img_seg"] = "media/upload/segmentation/output/img_seg.png"
            return render(request, "segmentacao_sucesso.html", context)
    else:
        form = FormSegmentation()

    context["form"] = form
    return render(request, template_name, context)


def similarity(request):
    return render(request, "similariedade.html")
