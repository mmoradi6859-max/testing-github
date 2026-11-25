#write login program
def login():    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # For demonstration purposes, we will use a hardcoded username and password
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Login failed. Please try again.")

if __name__ == "__main__":
    login()
    