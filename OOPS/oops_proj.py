

class chatbook:
    
    def __init__(self ):   
        self.username = "" 
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to chatbook!! How would you like to proceed? 1- Signup , 
                           2- Signin , 
                           3- Write a post , 
                           4- Message a friend , 
                           5- exit\n""")
        if user_input == "1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()
            
    def signup(self):
        email = input("Enter your email here\n")
        pwd = input("Setup your password\n")
        self.username = email
        self.password = pwd
        print('You have signed up successfully')
        print("\n")     
        self.menu()
        
    def signin(self):
        if self.username == '' and self.password  =='':
            print("Please signup first by pressing 1 in the main menu")       
        else:
            username = input("Enter your email/username") 
            pwd = input("Enter your password here")
            if self.username == username and self.password == pwd:
                self.loggedin = True
            else:
                print("Sign up first")
        print("\n")        
        self.menu()
                      
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here")
            print("Your post has been posted successfully")
        else:
            print("You need to sign in first")
        print("\n")
        self.menu()
        
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here")
            frnd = input("Whom to send the msg?")
            print(f"Your message has been sent to {frnd}")
        else:
            print("Sign in first")
        print("\n")        
        self.menu()
        
        
if __name__ == "__main__":
    obj = chatbook()

