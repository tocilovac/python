import sqlite3
from customer_signup import signup_customer   # From your customer_signup.py file
from shop import browse_cars  #  Make sure this line is present

# from cars import populate_cars_table  # Uncomment this ONCE if you want to add 50 cars initially

def main():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # --- Ensure Customers table exists ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID TEXT PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Email TEXT NOT NULL,
            Phone TEXT,
            Address TEXT
        )
    """)
    conn.commit()

    # --- Step 1: Register customer ---
    customer_id = signup_customer(cursor)
    conn.commit()

    # --- Step 2: Browse and select cars ---
    browse_cars(cursor)  # ✅ This shows your car inventory and lets customer pick

    conn.close()

if __name__ == '__main__':
    main()
