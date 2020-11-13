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
from django.urls import path,re_path
from zendesk_tickets_app.views import zendeskHome,zendeskConnect,zendeskticketDescription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', zendeskHome, name='HomeView'),
    path('connect/', zendeskConnect, name='ConnectView'),
    re_path(r'ticket/(?P<ticket_id>\d+)$', zendeskticketDescription, name='TicketDescriptionView'),
    path('connect/ticket', zendeskticketDescription, name = 'TicketDescriptionView'),
]
