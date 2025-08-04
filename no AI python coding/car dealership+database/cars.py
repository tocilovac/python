import sqlite3
import random
from datetime import datetime

def populate_cars_table(cursor):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # --- Create Cars table ---
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

    # --- Car attributes ---
    colors = ['Red', 'Black', 'White', 'Silver', 'Blue']
    brands_models = [
        ('Toyota', 'Corolla'), ('Toyota', 'Camry'), ('Honda', 'Civic'), ('Honda', 'Accord'),
        ('Hyundai', 'Elantra'), ('Hyundai', 'Sonata'), ('Mazda', '3'), ('Mazda', '6'),
        ('BMW', 'Series 3'), ('BMW', 'Series 5'), ('Mercedes', 'C-Class'), ('Mercedes', 'E-Class'),
        ('Kia', 'Sportage'), ('Kia', 'Optima'), ('Ford', 'Fusion'), ('Ford', 'Focus'),
        ('Audi', 'A3'), ('Audi', 'A4'), ('Chevrolet', 'Malibu'), ('Volkswagen', 'Jetta'),
        ('Nissan', 'Altima'), ('Nissan', 'Sentra'), ('Lexus', 'IS'), ('Lexus', 'ES'),
        ('Peugeot', '508')
    ]

    # --- Price generator ---
    def generate_price(brand):
        price_map = {
            'Toyota': (22000, 30000), 'Honda': (22000, 30000), 'Hyundai': (18000, 27000),
            'Mazda': (19000, 28000), 'BMW': (35000, 60000), 'Mercedes': (37000, 65000),
            'Kia': (17000, 24000), 'Ford': (20000, 29000), 'Audi': (33000, 58000),
            'Chevrolet': (19000, 27000), 'Volkswagen': (20000, 29000), 'Nissan': (20000, 28000),
            'Lexus': (38000, 63000), 'Peugeot': (24000, 32000)
        }
        low, high = price_map.get(brand, (20000, 30000))
        return round(random.uniform(low, high), 2)

    # --- Insert 50 cars ---
    for _ in range(50):
        brand, model = random.choice(brands_models)
        color = random.choice(colors)
        year = datetime.now().year
        price = generate_price(brand)

        cursor.execute("""
            INSERT INTO Cars (Model, Color, Brand, Year, Price)
            VALUES (?, ?, ?, ?, ?)
        """, (model, color, brand, year, price))

    conn.commit()
    conn.close()
