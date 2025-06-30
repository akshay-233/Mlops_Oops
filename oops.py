class Chatbook:

    __user_id=1

    def __init__(self):
        self.id=Chatbook.__user_id
        Chatbook.__user_id+=1
        self.username=''
        self.password=''
        self.loggedin=False 
        self.menu()

    @staticmethod
    def get_id():
        return Chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        Chatbook.__user_id=val

    def menu(self):
        user_input=input("""Welcome to Chatbook
              1. Press 1 to sign up
              2. Press 2 to sign in
              3. Press 3 to write a post
              4. Press 4 to message a friend
              5. Press 5 to exit""")
        if user_input==1:
            self.sign_up()
        if user_input==2:
            self.sign_in()
        if user_input==3:
            pass
        if user_input==4:
            pass
        if user_input==5:
            exit()

    def sign_up(self):
        email=input("Enter yor email")
        pwd=input("Enter your password")
        self.username=email
        self.password=pwd
        print("You have signed up successfull\n")
        self.menu()

    def sign_in(self):
        if self.username=='' and self.password=='':
            print("You have to sign up first in order to sig in")
        else:
            uname=input("Enter you email id: ")
            pwd=input("Enter your password: ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully!")
                self.loggedin=True
            else:
                print("You have entered the wrong credentials")
        print("\n")
        self.menu() 

    def post(self):
        if self.loggedin==True:
            txt=input("Please enter your post: ")
            print(f"You have posted the following content {txt}")
        else:
            print("Please sign in to share your thoughts")
        print("\n")
        self.menu()

    def message(self):
        if self.loggedin==True:
            txt=print("Enter the text here-> ")
            frnd=print("Enter the name of your friend-> ")
            print(f"The message {txt}\nhad been sent to {frnd}")
        else:
            print("Please sign in to send the message")
        print("\n")
        self.menu()
    

