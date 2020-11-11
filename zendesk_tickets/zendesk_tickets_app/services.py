import os
import requests

def get_tickets():
    url = 'https://sample4450.zendesk.com/api/v2/tickets.json'
    #url = 'https://.zendesk.com/api/v2/tickets.json'
    user = 'zendesk.coding.test@gmail.com' + '/token'
    pwd = 'bGYM6Oe1Z8zk2LbYdr3Eyv7E7lhaiz8LDjS7HMe9'

    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        return(response.status_code)
    else:
        tickets = response.json()
        tickets_list = []
        for i in range(len(tickets['tickets'])):
            tickets_list.append(tickets['tickets'][i])
        return tickets_list

def get_ticket_details(id):
    url = 'https://sample4450.zendesk.com/api/v2/tickets/'+id+'.json'
    user = 'zendesk.coding.test@gmail.com' + '/token'
    pwd = 'bGYM6Oe1Z8zk2LbYdr3Eyv7E7lhaiz8LDjS7HMe9'

    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        return(response.status_code)
    else:
        ticket = response.json()
        return ticket['ticket']
