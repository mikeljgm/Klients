import os
import pathlib
from datetime import datetime as dt

#VARIABLE FOR DATE
date = dt.now()

#CONSTANTS
ADD_NEW = 1
SEARCH_CUS = 2
ADD_PAY = 3
SHOW_ALL = 4
EXIT = 0
DATE = date.strftime("%A %d, %B %Y - %H:%M %p")

#MODULE FOR MENU
def menu():
    os.system('cls')
    print('     Klients')
    print('=' * 30)

    print(f'''
    {ADD_NEW}) Add new client
    {SEARCH_CUS}) Search client
    {ADD_PAY}) Add new payment
    {SHOW_ALL}) Show all clients
    {EXIT}) Exit
    ''')

#LOAD OR CREATE DATA BASE MODULE
def load_database(clients, data_base):
    if pathlib.Path(data_base).exists():
        file = open(data_base, 'r')

        for line in file:
            contact, phone_number, email, id_, product_type, price, DATE = linea.strip().split(',')
            clients[contact] = (phone_number, email, id_, product_type, price, DATE)
    else:
        file = open(data_base, 'w')
        pass

#ADD CLIENT MODULE
def add_client(clients, data_base):
    os.system('cls')
    print('     Adding New Client')
    print('=' * 30)

    if clients.get(name):
        print(f'Client: {name} already exist')
    else:
        name = input("Full name: ")


# file = open("db/" + name + "_" + id_ + ".txt", "w")
#git push -u origin main