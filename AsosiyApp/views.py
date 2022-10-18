from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Boss,Product
from django.http import JsonResponse
import json

# Create your views here.
def json(request):
    data={}
    data['Boss']=list((Boss.objects.values()))
    data['Product']=list((Product.objects.values()))

    return JsonResponse(data,safe=False)

class Index(TemplateView):
    template_name = 'index.html'



