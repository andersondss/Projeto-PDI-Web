from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def codification(request):
    return render(request, "codificacao.html")


def similarity(request):
    return render(request, "similariedade.html")


def segmentation(request):
    return render(request, "segmentacao.html")
