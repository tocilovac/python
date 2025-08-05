import sqlite3
import random
import string
import blessed
from blessed import Terminal

# Initialize the blessed terminal
term = Terminal()

def generate_customer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def signup_customer(cursor):
    print(f"\n{term.bold_cyan}--- Customer Registration ---\n{term.normal}")
    
    fname = input(f"{term.bold_cyan}First Name: {term.normal}").strip().title()
    lname = input(f"{term.bold_cyan}Last Name: {term.normal}").strip().title()
    email = input(f"{term.bold_cyan}Email: {term.normal}").strip()
    phone = input(f"{term.bold_cyan}Phone (optional): {term.normal}").strip()
    address = input(f"{term.bold_cyan}Address: {term.normal}").strip().title()

    customer_id = generate_customer_id()

    try:
        cursor.execute("""
            INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (customer_id, fname, lname, email, phone, address))

        print(f"\n{term.bold_green}Registration complete! Your Customer ID is: {customer_id}{term.normal}")
        return customer_id
    except sqlite3.IntegrityError as e:
        print(f"\n{term.bold_red}Error: A user with that email already exists. Please try again.{term.normal}")
        return None
