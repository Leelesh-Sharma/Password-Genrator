from cryptography.fernet import Fernet

def add():
    website = input("Website address - ")
    username = input("Username - ")
    password = input("Password - ")
    with open('pwd','a') as file:
        file.write(website+"|"+username+"|"+password+"\n")

def view():
    with open('pwd','r') as file:
        data = file.read()
        w,un,pd = data.split("|")
        print("Website-"+w+"\nusername-"+un+"\npassword-"+pd)

while True:
    action = input("\n What would you like to do \n for adding a password - type 'add' or for viewing them - type 'view' \n or press 'q' to quit.").lower()
    
    if action == 'q':
        break
    
    if action == 'add':
        add()
    elif action == 'view':
        view()
    else:
        print('Invalid action.')
        continue