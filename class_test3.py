
class User:
    def __init__(self, name="", email="", password=""):
        self.name = name
        self.email = email
        self.password = password
        self.logged_in = False   

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == self.email and password == self.password:
            self.logged_in = True
            print("Login Successful")
        else:
            print("Login Failed!")

    def logout(self):
        self.logged_in = False
        print("Logged out!")

    def is_logged_in(self):
        return self.logged_in

    def profile(self):
        if self.is_logged_in():
            print("Name:", self.name)
            print("Email:", self.email)
        else:
            print("User is not Logged in!")



user1 = User("Manjarul", "manjarulalam21.bd@gmail.com", "098712")

user1.login()      
user1.profile()    
user1.logout()     
user1.profile()    