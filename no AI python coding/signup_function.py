import string, random

def signup():
    while True:
        username = input("Enter a username:").strip()
        # Validations
        _ = 0
        for i in range(len(username)):
            if username[i] == " ":
                _ += 1
        
        if len(username) == 0:
            print("You must enter a username! Try again.")
            continue
        elif _ > 0:
            print ("username can't include empty spaces (you may use underlines(_) or dots(.) instead!")
            continue
        # later on if we add a file to store this data, we can add more conditions and rules for the username.
        break
        
    while True:
        # Random or personal password:
        user_choice = input("Do you want a randomly generated password (Type yes/no): ").strip().lower()
        if user_choice == "yes":
            chars = string.ascii_letters + string.digits + '!@#$%~()*-+'
            password = ''.join(random.choice(chars) for i in range (random.randint(5, 16)))
            break
        elif user_choice == 'no':
            pass
        else:
            print ("Wrong input! Please try again with 'yes' or 'no'.")
            continue

        password = input("Enter a password:").strip()
        if len(password) < 5:
            print("Password too short, minimum 5 chars")
            continue
    
        confirm_password = input("Confirm your password: ").strip()
        if password != confirm_password:
            print("Password did not match. Please try again.")
        else:
            break
    return username, password
    
username, password = signup()
print("Signup successful")
print("Username:", username)
print("Password:", password)