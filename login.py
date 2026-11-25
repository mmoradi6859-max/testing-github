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

#add a feature to allow users to create a new account
def create_account():
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")

    # Here you would normally save the new account details to a database or file
    print(f"Account created successfully for username: {new_username}") 
