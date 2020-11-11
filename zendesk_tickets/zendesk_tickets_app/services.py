import os
import requests

def get_tickets():
    url = 'https://sample4450.zendesk.com/api/v2/tickets.json'
    user = 'zendesk.coding.test@gmail.com' + '/token'
    pwd = 'bGYM6Oe1Z8zk2LbYdr3Eyv7E7lhaiz8LDjS7HMe9'

    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
    else:
        tickets = response.json()
        tickets_list = []
        for i in range(len(tickets['tickets'])):
            tickets_list.append(tickets['tickets'][i])
        #print(tickets_list[0])
        return tickets_list
