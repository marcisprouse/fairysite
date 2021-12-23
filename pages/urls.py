from django.urls import path
from django.views.generic import TemplateView
from .views import About, Index

app_name='pages'

urlpatterns = [
    path('', Index.as_view(template_name="pages/index.html"), name='home'),
    path('pages/about', About.as_view(template_name="pages/about.html"), name='about'),
    path('pages/portfolio', TemplateView.as_view(template_name="pages/portfolio.html"), name='portfolio'),
]

handler404="home.views.handle_not_found"

