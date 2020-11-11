from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .services import get_tickets,get_ticket_details
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import JsonResponse
# Create your views here.

# class zendeskHome(TemplateView):
#     template_name = 'home.html'

# class zendeskConnect(TemplateView):
#     template_name = 'connect.html'
#     def get_context_data(self, *args, **kwargs):
#         context = {
#             'tickets' : get_tickets(),
#         }
#         return context
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

def zendeskHome(request):
    return render(request,'home.html')

def zendeskConnect(request):
    #tickets = get_tickets()
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



def ticketDescription(request):
    if request.method == 'GET':
        ticket_id = request.GET.get('ticket_id')
        #print(ticket_id)
        ticket_details = get_ticket_details(ticket_id)
        #print(ticket_details)
        return JsonResponse(ticket_details)
