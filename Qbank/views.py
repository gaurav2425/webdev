from django.shortcuts import render
from django.http import HttpResponse
from .models import QbankModel



def home(request):
    Qbank = QbankModel.objects.all()
    return render(request, 'home.html', {'Qbank': Qbank})



def about(request):
     Qbank = QbankModel.objects.all()
     return render(request, 'about.html', {'Qbank': Qbank})



def ABIO(request):
    return render(request, 'ABIO.html')



def results(request):
    return render(request, 'results.html')