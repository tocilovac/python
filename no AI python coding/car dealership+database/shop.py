def browse_cars(cursor):
    print("\n--- Car Inventory ---")
    cursor.execute("SELECT CarID, Model, Brand FROM Cars")
    cars = cursor.fetchall()

    for car in cars:
        print(f"ID: {car[0]}, Model: {car[1]}, Brand: {car[2]}")

    while True:
        selected_model = input("\nChoose a car model from above: ").strip().title()
        selected_brand = input("Choose a brand: ").strip().title()

        cursor.execute("""
            SELECT CarID, Model, Brand, Color, Year, Price FROM Cars
            WHERE Model = ? AND Brand = ?
        """, (selected_model, selected_brand))
        matches = cursor.fetchall()

        if not matches:
            print("😕 No matching cars found for that model and brand.")
            try_again = input("Do you want to try again? (yes/no): ").strip().lower()
            if try_again != "yes":
                print("Returning to main menu...")
                break
            continue

        print("\n--- Available Variants ---")
        for car in matches:
            print(f"ID: {car[0]}, Color: {car[3]}, Year: {car[4]}, Price: ${car[5]}")

        chosen_color = input("\nEnter preferred color: ").strip().title()
        chosen_year = int(input("Enter preferred year: ").strip())

        cursor.execute("""
            SELECT * FROM Cars
            WHERE Model = ? AND Brand = ? AND Color = ? AND Year = ?
        """, (selected_model, selected_brand, chosen_color, chosen_year))
        final_choice = cursor.fetchone()

        if final_choice:
            print(f"\n🎉 Perfect match found!\nModel: {final_choice[1]}, Color: {final_choice[2]}, Year: {final_choice[4]}, Price: ${final_choice[5]}")
        else:
            print("No car matches your exact selection.")
            try_again = input("Do you want to try again with another variant? (yes/no): ").strip().lower()
            if try_again != "yes":
                print("Returning to main menu...")
                break
        break
        print("Invalid input. Please try again.")
