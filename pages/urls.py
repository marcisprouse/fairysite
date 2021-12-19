from django.urls import path
from django.views.generic import TemplateView

app_name='pages'

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/index.html"), name='home'),
    path('pages/about', TemplateView.as_view(template_name="pages/about.html"), name='about'),
    path('pages/portfolio', TemplateView.as_view(template_name="pages/portfolio.html"), name='portfolio'),
]

handler404="home.views.handle_not_found"

