from django.urls import path

from django.views.generic.base import TemplateView

app_name = 'pages'

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home_page.html'), name='home-page'),
]
