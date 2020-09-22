from django.shortcuts import render
from django.http import HttpResponse
from .models import QbankModel



def home(request):

    Qbank = QbankModel.objects.all()
    Qbank = QbankModel.objects.all()
    return render(request, 'home.html', {'Qbank': Qbank})



def about(request):
    return render(request, 'about.html', {'title': 'Qbank'})
