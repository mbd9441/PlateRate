from django.shortcuts import render
from django.http import HttpResponse
from ..models import Documentation

def doclist(request):
    doc_list = Documentation.objects.order_by('Doc_Type')
    context = {'doc_list':doc_list}
    return render(request, 'platerateapp/documentation.html', context)
