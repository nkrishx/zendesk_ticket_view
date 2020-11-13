from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .services import get_tickets,get_ticket_details
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import JsonResponse,HttpResponse
# Create your views here.

def zendeskHome(request):
    #home page view
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
        #render the page not found template if passed wrong API request url
        return render(request, 'exception.html')


def zendeskticketDescription(request, ticket_id=None):
    #ticket description view, return the HTTP Resposne to bypass exception thrown during ticketview pagination rendering
    if ticket_id:
        ticket_details = get_ticket_details(ticket_id)
        return render(request,'ticket_details.html',{'ticket_details':ticket_details})
    else:
        return HttpResponse(status=204)
