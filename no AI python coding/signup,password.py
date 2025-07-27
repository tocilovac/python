def signup():
    username = input("Enter a username: ").strip()  # .strip() removes spaces from both ends
    password = input("Enter a password: ").strip()
    return username, password  # return sends values back to caller

username, password = signup()  # ← THIS LINE CALLS THE FUNCTION

print("Signup successful!")
print("Username:", username)
print("Password:", password) 


def signup():
    username = input("enter a username:").strip()
    
    while True: # while True: creates an endless loop that keeps running until a 'break' statement stops it
        password = input("enter a password:").strip()
        if len(password) < 5:
            print("password too short, minimum 5 chars")
        else:
            break #password is fine and exits the loop
    return username, password 
username, password = signup()
print("signup successful")
print("username:", username)
print("password:", password)


def signup():
    username = input("enter a username:").strip()
    
    while True:
        password = input("enter a password:").strip()
        if len(password) < 5:
            print("password too short, minimum 5 chars")
            continue # Go back to the top and ask for password again
    
        confirm_password = input("confirm your password:").strip()
        if password != confirm_password:
            print("password did not match.please try again.")
        else:
            break # Only reached if both checks are passed
    
    return username, password
username, password = signup()
print("signup successful")
print("username:", username)
print("password:", password)


users = {}# users = {} creates a dictionary to store username-password pairs
def signup():
    username = input("Enter a username: ").strip()
    
    if username in users:# if username in users: checks if the chosen username already exists
        print("Username already exists. Please choose another one.")
        return None, None # return None, None exits the function early if signup fails
    while True:
        password = input("enter a password:").strip()
        if len(password) < 5:
            print("Password too short, minimum 5 chars")
            continue 
        confirm_password = input("confirm your password:").strip()
        if password != confirm_password:
            print("Password did not match. Please try again.")
        else:
            break
    users[username] = password  # Store the username and password in the dictionary
    return username, password
username, password = signup()
if username and password:
    print("Signup successful")
    print("Username:", username)
    print("Password:", password)
    print("all users:", users)  # Display all users for verification











