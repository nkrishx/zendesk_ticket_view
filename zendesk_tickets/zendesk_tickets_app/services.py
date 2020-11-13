import os
import requests

def get_tickets():
    #service function to retrieve all tickets from the account
    #url to access the tickets from the account, API call with API token setup from zendesk account.

    url = 'https://sample4450.zendesk.com/api/v2/tickets.json'
    #url = 'https://.zendesk.com/api/v2/tickets.json'    #broken url to check the rendering of exception.html template
    user = 'zendesk.coding.test@gmail.com' + '/token'
    pwd = 'bGYM6Oe1Z8zk2LbYdr3Eyv7E7lhaiz8LDjS7HMe9'

    response = requests.get(url, auth=(user, pwd))

    if response.ok:
        tickets = response.json()
        tickets_list = []
        for i in range(len(tickets['tickets'])):
            tickets_list.append(tickets['tickets'][i])
        return tickets_list                            #return list of all tickets from the account
    else:
        return None

def get_ticket_details(id):
    #service function to retrieve a single tickets information
    #id contains the value(id) of the ticket's complete description to be retrieved

    url = 'https://sample4450.zendesk.com/api/v2/tickets/'+id+'.json'
    user = 'zendesk.coding.test@gmail.com' + '/token'
    pwd = 'bGYM6Oe1Z8zk2LbYdr3Eyv7E7lhaiz8LDjS7HMe9'

    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        return(response.status_code)
    else:
        ticket = response.json()
        return ticket['ticket']
