from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .services import get_tickets,get_ticket_details
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import JsonResponse
# Create your views here.

def zendeskHome(request):
    return render(request,'home.html')

def zendeskConnect(request):
    try:
        #exception handling
        tickets = get_tickets()
        paginator = Paginator(tickets, 25)
        page = request.GET.get('page')
        try:
            tickets = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tickets = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tickets = paginator.page(paginator.num_pages)

        #page_obj = paginator.get_page(page_number)
        return render(request, 'connect.html', {'tickets': tickets})
    except:
        return render(request, 'exception.html')


def zendeskticketDescription(request):
    #check if ajax request and get the id of the ticket. Sanity check
    if request.method == 'GET' and request.is_ajax():
        ticket_id = request.GET.get('ticket_id')
        ticket_details = get_ticket_details(ticket_id)
        return JsonResponse(ticket_details)
