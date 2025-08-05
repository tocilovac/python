import sqlite3
import blessed
from blessed import Terminal
from customer_signup import signup_customer
from shop import browse_cars
from cars import populate_cars_table

# Initialize the blessed terminal
term = Terminal()

# --- Defines the main menu parameters and navigation ---
def main_menu(options, index):
    with term.cbreak():
        index = 0
        while True:
            print(term.clear() + term.move_yx(0, 0))
            print(term.bold_red("Car Dealership Program - Main Menu\n"))
            
            for i, option in enumerate(options):
                if i == index:
                    print(f"{term.bold_purple}{term.reverse}{option}{term.normal}")
                else:
                    print(option)
            
            key = term.inkey()
            if key.name == 'KEY_UP' or key.name == 'KEY_LEFT':
                index = (index - 1) % len(options)
            elif key.name == 'KEY_DOWN' or key.name == 'KEY_RIGHT':
                index = (index + 1) % len(options)
            elif key.name == 'KEY_ENTER':
                print(term.clear())
                return index

def main():
    conn = None
    try:
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # --- Ensure tables exist ---
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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cars (
                CarID INTEGER PRIMARY KEY AUTOINCREMENT,
                Model TEXT NOT NULL,
                Color TEXT NOT NULL,
                Brand TEXT NOT NULL,
                Year INTEGER NOT NULL,
                Price REAL NOT NULL
            )
        """)
        conn.commit()

        while True:
            options = ["Register Customer", "Browse Cars", "Populate Cars Table (Run this once)", "Quit"]
            selected_index = main_menu(options, 0)
            
            if selected_index == 0:
                print(f"{term.bold_yellow}--- Customer Registration ---\n{term.normal}")
                signup_customer(cursor)
                conn.commit()
                input(f"\n{term.dim}{term.yellow}Press Enter to return to the main menu...{term.normal}")
            
            elif selected_index == 1:
                print(f"{term.bold_yellow}--- Car Inventory ---\n{term.normal}")
                browse_cars(cursor)
                conn.commit()
                input(f"\n{term.dim}{term.yellow}Press Enter to return to the main menu...{term.normal}")

            elif selected_index == 2:
                print(f"{term.bold_yellow}--- Populating Cars Table ---\n{term.normal}")
                populate_cars_table(cursor)
                conn.commit()
                print(f"{term.bold_green}Successfully populated the Cars table!{term.normal}")
                input(f"\n{term.dim}{term.yellow}Press Enter to return to the main menu...{term.normal}")

            elif selected_index == 3:
                print(f"\n{term.bold_yellow}Goodbye!{term.normal}\n")
                break

    except sqlite3.Error as e:
        print(f"{term.bold_red}Database error: {e}{term.normal}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
