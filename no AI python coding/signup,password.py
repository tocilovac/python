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
            continue
    
        confirm_password = input("confirm your password:").strip()
        if password != confirm_password:
            print("password did not match.please try again.")
        else:
            break
    
    return username, password
username, password = signup()
print("signup successful")
print("username:", username)
print("password:", password)
    



