class User:
    name = ""
    email = ""
    password = ""
    logged_in = "False"

    def login(self):
        email = input("enter your email")
        password = input("enter your password")

        if email == self.email and password==self.password:
            logged_in = True
            print("Login Succesful")
        else: 
            print("Login Failed!")


    def logout(self):
        self.logged_in = False
        print("Logged out!")

    def isloggedin(self):
        if self.logged_in:
            return True
        else:
            return False

    def profile(self):
        if self.isloggedin():
            print("Name:",self.name)
            print("Email:",self.email)
        else:
            print("User is not Logged in!")    

user1 = User()

user1.name = "Manjarul"
user1.email = "manjarulalam21.bd@gmail.com"
user1.password = "098712"


user1.login()
user1.logout()
user1.isloggedin()
user1.profile()
         






