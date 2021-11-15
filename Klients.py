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
        phone_number = input("Phone number: ")
        email = input("Email: ")
        id_ = input("Identification: ")
        product_type = input("Product type: ")
        price = input("Price: ")

        clients[os.name] = (phone_number, email, id_, product_type, price, DATE) 
        file = open('data_base', 'a')
        file.write(f'{name}, {phone_number}, {email}, {id_}, {product_type}, {price}, {DATE}\n')
        print('\n**** Contacto agregado con exito ****\n')

#SHOW CONTACTS METHOD
def show_contacts():
    os.system('cls')
    print('     Adding New Client')
    print('=' * 30)

    if len(data_base) > 0:
        for contact, data in data_base.items():
            print(f'Name: {contact}')
            print(f'Phone: {data[0]}')
            print(f'Email: {data[1]}')
            print(f'ID: {data[2]}')
            print(f'Product: {data[3]}')
            print(f'Price: {data[4]}')
            print(f'Date: {data[5]}')
            print('=' * 40)
    else :
        print('There are no contact registered.')

#SEARCH CONTACT METHOD
def search_contac():
           
# file = open("db/" + name + "_" + id_ + ".txt", "w")
#git push -u origin main