"""KidSmiley URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name='home'),
    url(r'^get-involved/$', TemplateView.as_view(template_name='home/get_involved.html'), name='get_involved'),
    url(r'^contact-us/$', TemplateView.as_view(template_name='home/contact.html'), name='contact_us'),
    url(r'^donate/$', TemplateView.as_view(template_name='home/donate.html'), name='donate'),
    url(r'^about-us/$', TemplateView.as_view(template_name='home/about.html'), name='about_us'),
]
