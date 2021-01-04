def login(username, pwd):
    LoggedIn = False
    while not LoggedIn:
        #equivalente di una console.readLine()
        u = str(input("username: ").lower())
        if u == username:
            if input("password: ") == pwd:
                print((username + " logged in"))
                LoggedIn = True
            else:
                print("wrong password")
        else:
            print("username sconosciuto")
#MAIN
login("nellaccia","12345")