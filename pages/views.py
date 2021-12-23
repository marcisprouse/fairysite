from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


