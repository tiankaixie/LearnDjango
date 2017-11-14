from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, WebPage
from . import forms

# Create your views here.

def index (request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'first_app/index.html', context = date_dict)

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'first_app/register.html', {'form', form})
