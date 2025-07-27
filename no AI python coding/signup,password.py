def signup():
    username = input("Enter a username: ").strip()  # .strip() removes spaces from both ends
    password = input("Enter a password: ").strip()
    return username, password  # return sends values back to caller

username, password = signup()  # ← THIS LINE CALLS THE FUNCTION

print("Signup successful!")
print("Username:", username)
print("Password:", password) 



