import re
import hashlib
import os
import sqlite3
from getpass import getpass
from colorama import Fore, Style, init

init(autoreset=True)
DB_NAME = "users.db"

class PasswordAdvisor:
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "qwerty", "abc123", "letmein", "welcome"
        ]
        self.strength_labels = {
            0: (Fore.RED + "❌ Risky", "Consider strengthening"),
            1: (Fore.RED + "❌ Weak", "Easy to compromise"),
            2: (Fore.YELLOW + "⚠️ Fair", "Could be stronger"),
            3: (Fore.YELLOW + "⚠️ Good", "Meets basic standards"),
            4: (Fore.GREEN + "✅ Strong", "Hard to crack"),
            5: (Fore.GREEN + "✅ Robust", "Excellent security")
        }

    def analyze(self, password):
        return {
            "length": len(password),
            "has_upper": bool(re.search(r'[A-Z]', password)),
            "has_lower": bool(re.search(r'[a-z]', password)),
            "has_digit": bool(re.search(r'\d', password)),
            "has_special": bool(re.search(r'[^A-Za-z0-9]', password)),
            "is_common": password.lower() in self.common_passwords,
            "has_repeats": bool(re.search(r'(.)\1{2,}', password))
        }

    def calculate_score(self, analysis):
        score = 0
        if analysis["length"] >= 12: score += 2
        elif analysis["length"] >= 8: score += 1
        if analysis["has_upper"]: score += 1
        if analysis["has_lower"]: score += 1
        if analysis["has_digit"]: score += 1
        if analysis["has_special"]: score += 1
        if analysis["is_common"]: score = max(0, score - 2)
        if analysis["has_repeats"]: score = max(0, score - 1)
        return min(5, score)

    def generate_report(self, password):
        analysis = self.analyze(password)
        score = self.calculate_score(analysis)
        label, description = self.strength_labels[score]

        report = [
            f"\n{Style.BRIGHT}Password Analysis{Style.RESET_ALL}",
            f"{label}: {description} ({score}/5)",
            f"Length: {analysis['length']} characters"
        ]

        positives = []
        if analysis["length"] >= 8:
            positives.append("✓ Meets minimum length")
        if analysis["has_upper"] and analysis["has_lower"]:
            positives.append("✓ Has both cases")
        if analysis["has_digit"]:
            positives.append("✓ Contains numbers")
        if analysis["has_special"]:
            positives.append("✓ Includes special characters")

        if positives:
            report.append(Fore.GREEN + "\nStrengths:")
            report.extend(f"- {p}" for p in positives)

        suggestions = []
        if analysis["length"] < 12:
            suggestions.append("Consider 12+ characters for stronger security")
        if not analysis["has_special"]:
            suggestions.append("Add symbols (!@#$) for robustness")
        if analysis["is_common"]:
            suggestions.append("Avoid common passwords")
        if analysis["has_repeats"]:
            suggestions.append("Reduce repeated characters")

        if suggestions:
            report.append(Fore.YELLOW + "\nSuggestions:")
            report.extend(f"- {s}" for s in suggestions)

        return "\n".join(report), score

# ──────────────────────────────────────────────────────────

def create_user_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            salt TEXT,
            hashed_password TEXT
        );
    """)
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    salt = salt or os.urandom(16).hex()
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return salt, hashed

def signup(advisor):
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip().lower()
    password = getpass("Create a password: ")

    report, score = advisor.generate_report(password)
    print(report)

    choice = input("\nDo you want to continue with this password? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Signup cancelled.")
        return

    salt, hashed = hash_password(password)

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name, email, salt, hashed_password) VALUES (?, ?, ?, ?)",
                  (name, email, salt, hashed))
        conn.commit()
        print(Fore.GREEN + "✅ Signup successful!")
    except sqlite3.IntegrityError:
        print(Fore.RED + "❌ Email already exists.")
    conn.close()

def login():
    email = input("Enter your email: ").strip().lower()
    password = getpass("Enter your password: ")

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT salt, hashed_password FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()

    if not row:
        print(Fore.RED + "❌ User not found.")
        return

    salt, stored_hash = row
    _, input_hash = hash_password(password, salt)

    if input_hash == stored_hash:
        print(Fore.GREEN + "🔓 Login successful!")
    else:
        print(Fore.RED + "❌ Incorrect password.")

# ──────────────────────────────────────────────────────────

def main():
    create_user_table()
    advisor = PasswordAdvisor()

    while True:
        print(Fore.CYAN + "\nWelcome to SecureAuth ✨")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Quit")
        action = input("Choose an option: ")

        if action == "1":
            signup(advisor)
        elif action == "2":
            login()
        elif action == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
