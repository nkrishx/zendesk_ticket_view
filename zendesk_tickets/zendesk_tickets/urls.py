"""zendesk_tickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zendesk_tickets_app.views import zendeskHome,zendeskConnect,ticketDescription

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', zendeskHome.as_view(template_name='home.html'), name='HomeView'),
    #path(r'connect/', zendeskConnect.as_view(template_name='connect.html'), name='ConnectView'),
    path('', zendeskHome, name='HomeView'),
    path(r'connect/', zendeskConnect, name='ConnectView'),
    path(r'connect/ticket', ticketDescription, name = 'TicketDescriptionView'),
]
