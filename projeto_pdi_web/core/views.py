import cv2
from django.shortcuts import render, redirect
from projeto_pdi_web.core.forms import FormCodification
from matplotlib import pyplot as plt
from projeto_pdi_web.core.models import Codification

def home(request):
    return render(request, "home.html")


def codification(request):

    template_name = "codificacao.html"
    context = {}
    if request.method == "POST":
        form = FormCodification(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            processSIFT(request.FILES["image"])
            # return redirect("core:home")
    else:
        form = FormCodification()

    context["form"] = form
    return render(request, template_name, context)


def similarity(request):
    return render(request, "similariedade.html")


def segmentation(request):
    return render(request, "segmentacao.html")


def processSIFT(image):

    print "upload/codification/"+image.name
    img = cv2.imread("upload/codification/"+image.name, 0)
    
    plt.imshow(img, cmap='gray')
    plt.show()
