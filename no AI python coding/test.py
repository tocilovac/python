users = {}  # Dictionary to store username-password pairs

def signup():
    username = input("enter a username:").strip()
    if username in users:  # Check if the username already exists
        print("Username already exists. Please choose another one.")
        return None, None
    
    while True:
        password = input("enter a password:").strip()
        if len(password) < 5:
            print("Password too short, minimum 5 chars")
            continue
        confirm_password = input("confirm your password:").strip()
        if password != confirm_password:
            print("Password did not match. Please try again.")
        else:
            break  # Exit loop once password checks are successful
    
    users[username] = password  # ✅ Save the user after password confirmation
    return username, password

def login():
    username = input("enter your username:").strip()
    password = input("enter your password:").strip()
    
    if users.get(username) == password:
        print("Login successful!")
    else:
        print("Login failed. Incorrect username or password.")

# Main loop
while True:
    print("welcome! please choose an option:")
    print("1. signup")
    print("2. login")
    print("3. exit")
    
    choice = input("enter your choice (1/2/3): ").strip()
    
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
        break  # 🔚 Exit the loop gracefully
    else:
        print("invalid choice. please enter 1, 2, or 3.")
