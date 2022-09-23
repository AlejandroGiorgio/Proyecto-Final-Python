from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    doc=loader.get_template('index.html')
    doc2=doc.render()
    return HttpResponse(doc2)