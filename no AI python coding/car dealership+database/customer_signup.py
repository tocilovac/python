import sqlite3, random, string

def generate_customer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def signup_customer(cursor):
    print("\n--- Customer Registration ---")
    fname = input("First Name: ").strip().title()
    lname = input("Last Name: ").strip().title()
    email = input("Email: ").strip()
    phone = input("Phone (optional): ").strip()
    address = input("Address: ").strip().title()

    customer_id = generate_customer_id()

    cursor.execute("""
        INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (customer_id, fname, lname, email, phone, address))

    print(f"\n Registration complete! Your Customer ID is: {customer_id}")
    return customer_id
