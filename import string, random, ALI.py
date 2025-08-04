import string, random
import sqlite3
import blessed
from blessed import Terminal
from datetime import datetime

term = Terminal()

def main():
    conn = None
    try:
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        
        while True:
            # Main menu options
            options = ["Sign Up a New User", "View All Users", "Quit"]
            selected_index = main_menu(options, 0)
            
            if selected_index == 0:
                # Sign Up a New User
                user = get_user(cursor)
                if user:
                    # SQL INSERT statement with placeholders for dynamic data
                    sql = """
                    INSERT INTO accounts (username, first_name, last_name, gender, signup_date, password) 
                    VALUES (?, ?, ?, ?, ?, ?)
                    """
                    
                    # The values to be inserted, passed as a tuple
                    values = (
                        user['username'],
                        user['fname'],
                        user['lname'],
                        user['gen'],
                        user['time'],
                        user['password']
                    )
                    
                    cursor.execute(sql, values)
                    conn.commit()
                    
                    print(f"\n{term.bold_green}Successfully added new user: {user['username']}\n")
                
            elif selected_index == 1:
                # View All Users
                view_all_users(cursor)

            elif selected_index == 2:
                # Quit the program
                print(f"\n{term.bold_yellow}Goodbye!\n")
                break

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

# --- Defines the main menu parameters and navigation ---
def main_menu(options, index):
    with term.cbreak():
        index = 0
        while True:
            print(term.clear() + term.move_yx(0, 0))
            print(term.bold_red("Choose an action:") + "\n")
            
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

# --- Displays all users in the accounts table ---
def view_all_users(cursor):
    try:
        cursor.execute("SELECT id, username, first_name, last_name, gender, signup_date FROM accounts")
        users = cursor.fetchall()
        
        if not users:
            print(f"\n{term.bold_yellow}No users found in the database.\n")
        else:
            print(f"\n{term.bold_blue}--- All Users ---\n")
            for user in users:
                print(f"{term.bold_cyan}ID: {user[0]}, Username: {user[1]}, Name: {user[2]} {user[3]}, Gender: {user[4]}, Signup Date: {user[5]}")
            print("\n" + term.bold_blue + "-" * 17 + "\n")
            
    except sqlite3.Error as e:
        print(f"Failed to fetch users: {e}")
    finally:
        input(f"{term.dim}{term.yellow}Press Enter to return to the main menu...")


class signup:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def username(self, cursor):
        while True:
            username = input(f"{term.bold_cyan}Enter a username: {term.normal}").strip()
            
            # --- Check for existing username in the database ---
            cursor.execute("SELECT COUNT(*) FROM accounts WHERE username = ?", (username,))
            if cursor.fetchone()[0] > 0:
                print(f"{term.bold_red}The username '{username}' is already taken. Please try again.{term.normal}")
                continue

            # Validations
            if len(username) == 0:
                print(f"{term.bold_red}You must enter a username! Try again.{term.normal}")
                continue
            elif ' ' in username:
                print(f"{term.bold_red}Username can't include empty spaces (you may use underlines(_) or dots(.) instead!){term.normal}")
                continue
            
            return username

    def password(self):
        while True:
            # Random or personal password:
            user_choice = input(f"{term.bold_cyan}Do you want a randomly generated password (Type yes/no): {term.normal}").strip().lower()
            if user_choice == "yes":
                chars = string.ascii_letters + string.digits + '!@#$%~()*-+'
                password = ''.join(random.choice(chars) for i in range(random.randint(5, 16)))
                break
            elif user_choice == 'no':
                while True:
                    password = input(f"{term.bold_cyan}Enter a password: {term.normal}").strip()
                    if len(password) < 5:
                        print(f"{term.bold_red}Password too short, minimum 5 chars{term.normal}")
                        continue
                
                    confirm_password = input(f"{term.bold_cyan}Confirm your password: {term.normal}").strip()
                    if password != confirm_password:
                        print(f"{term.bold_red}Password did not match. Please try again.{term.normal}")
                    else:
                        break
                break
            else:
                print(f"{term.bold_red}Wrong input! Please try again with 'yes' or 'no'.{term.normal}")
                continue
        return password

def get_user(cursor):
    first_name = input(f"{term.bold_cyan}Enter your first name: {term.normal}").title()
    last_name = input(f"{term.bold_cyan}Enter your last name: {term.normal}").title()
    user_gender = input(f"{term.bold_cyan}Enter your gender: {term.normal}").title()
    user = signup(first_name, last_name, user_gender)
    fname = user.fname
    lname = user.lname
    gen = user.gender
    
    # Pass the cursor to the username method for validation
    username = user.username(cursor)
    
    password = user.password()
    signup_time = datetime.now()
    signup_time = signup_time.strftime("%Y-%m-%d %H:%M:%S")
    return {'fname': fname, 'lname': lname, 'gen': gen, 'username': username, 'password': password, 'time': signup_time}

if __name__ == '__main__':
    main()
