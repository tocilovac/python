users = {} 

def signup():
    username = input("enter a username:").strip()
    if username in users:
        print("username already exists. please choose another one.")
        return None, None
    
    while True:
        password = input("enter a password:").strip()
        if len(password) < 5:
            print("password too short,minimum 5 chars.")
            continue
        confirm_password = input("confirm your password:").strip()
        if password != confirm_password:
            print("password does not match. try again.")
        else:
            break
    
    users[username] = password
    return username, password 

def login():
    username = input("enter your username:").strip()
    password = input("enter your password:").strip()
    
    if users.get(username) == password:
        print("login successful!")
    else:
        print("login failed, incorrect username or password.")

def main():
    while True:
        print("\nwelcome!, please choose an option:")
        print("1. signup")
        print("2. login")
        print("3. exit")
        
        choice = input("enter your choice (1/2/3):").strip()
        
        if choice == "1":
            username, password = signup()
            if username and password:
                print("signup successful.")
                print("username:", username)
                print("password:", password)
                print("all users:", users)
        elif choice == "2":
            login()
        elif choice == "3":
            print("goodbye!")
            break
        else:
            print("invalid choice. please enter 1, 2, or 3.")
            
if __name__ == "__main__":
    main()
# authentication system clean code.py
# This code implements a simple authentication system with signup and login functionalities.
