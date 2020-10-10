from django.shortcuts import render
from django.http import HttpResponse
from .models import QbankModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView



def home(request):
    Qbank = QbankModel.objects.all()
    return render(request, 'home.html', {'Qbank': Qbank})




def about(request):
     Qbank = QbankModel.objects.all()
     return render(request, 'about.html', {'Qbank': Qbank})



def ABIO(request):
    return render(request, 'ABIO.html')


@login_required
def results(request):
    return render(request, 'results.html')

@method_decorator(login_required, name='dispatch')
class QbankListView(ListView):
    model = QbankModel
    template_name = 'qbankview.html'
    context_object_name = 'Qbank'