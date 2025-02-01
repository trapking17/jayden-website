accounts ={"Test" : "Test1", "Test2" : "Password"}

username = input("Please enter your username: ")
password = input("Please enter the password for " + username + ": ")

if (accounts.get(username) == password):
    print("Login Succesful")
    test = input(".") #This is just so the program doesn'nt shut down as soon as you get the username and password correct
else:
    print("Login failed")
