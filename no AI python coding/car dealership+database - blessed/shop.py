import blessed
from blessed import Terminal

# Initialize the blessed terminal
term = Terminal()

def browse_cars(cursor):
    print(f"{term.bold_yellow}\n--- Car Inventory ---\n{term.normal}")
    cursor.execute("SELECT CarID, Model, Brand FROM Cars")
    cars = cursor.fetchall()
    
    if not cars:
        print(f"{term.bold_red}No cars found in the inventory.{term.normal}")
        return

    for car in cars:
        print(f"{term.bold_cyan}ID: {car[0]}, Model: {car[1]}, Brand: {car[2]}{term.normal}")

    while True:
        selected_model = input(f"{term.bold_cyan}\nChoose a car model from above: {term.normal}").strip().title()
        selected_brand = input(f"{term.bold_cyan}Choose a brand: {term.normal}").strip().title()

        cursor.execute("""
            SELECT CarID, Model, Brand, Color, Year, Price FROM Cars
            WHERE Model = ? AND Brand = ?
        """, (selected_model, selected_brand))
        matches = cursor.fetchall()

        if not matches:
            print(f"{term.bold_red}😕 No matching cars found for that model and brand.{term.normal}")
            try_again = input(f"{term.bold_yellow}Do you want to try again? (yes/no): {term.normal}").strip().lower()
            if try_again != "yes":
                print(f"{term.dim}{term.yellow}Returning to main menu...{term.normal}")
                break
            continue

        print(f"\n{term.bold_yellow}--- Available Variants ---\n{term.normal}")
        for car in matches:
            print(f"{term.bold_cyan}ID: {car[0]}, Color: {car[3]}, Year: {car[4]}, Price: ${car[5]}{term.normal}")

        chosen_color = input(f"{term.bold_cyan}\nEnter preferred color: {term.normal}").strip().title()
        chosen_year_input = input(f"{term.bold_cyan}Enter preferred year: {term.normal}").strip()
        
        try:
            chosen_year = int(chosen_year_input)
        except ValueError:
            print(f"{term.bold_red}Invalid year format. Please enter a number.{term.normal}")
            continue

        cursor.execute("""
            SELECT * FROM Cars
            WHERE Model = ? AND Brand = ? AND Color = ? AND Year = ?
        """, (selected_model, selected_brand, chosen_color, chosen_year))
        final_choice = cursor.fetchone()

        if final_choice:
            print(f"\n{term.bold_green}🎉 Perfect match found!{term.normal}\n{term.bold_cyan}Model: {final_choice[1]}, Color: {final_choice[2]}, Year: {final_choice[4]}, Price: ${final_choice[5]}{term.normal}")
        else:
            print(f"{term.bold_red}No car matches your exact selection.{term.normal}")
            try_again = input(f"{term.bold_yellow}Do you want to try again with another variant? (yes/no): {term.normal}").strip().lower()
            if try_again != "yes":
                print(f"{term.dim}{term.yellow}Returning to main menu...{term.normal}")
                break
        break

def delete_cars_and_reset_sequence(cursor):
    """Deletes all entries from the Cars table and resets the auto-increment counter."""
    try:
        # Delete all rows from the Cars table
        cursor.execute("DELETE FROM Cars")
        
        # Reset the auto-increment sequence for the Cars table
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'Cars'")
        
        print(f"{term.bold_green}All cars have been deleted and the sequence has been reset.{term.normal}")
    except sqlite3.Error as e:
        print(f"{term.bold_red}Error deleting cars or resetting sequence: {e}{term.normal}")
