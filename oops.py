class Chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False 
        self.menu()

    def menu(self):
        user_input=input("""Welcome to Chatbook
              1. Press 1 to sign up
              2. Press 2 to sign in
              3. Press 3 to write a post
              4. Press 4 to message a friend
              5. Press 5 to exit""")
        if user_input==1:
            pass
        if user_input==2:
            pass
        if user_input==3:
            pass
        if user_input==4:
            pass
        if user_input==5:
            exit()

obj=Chatbook()