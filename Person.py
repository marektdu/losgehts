class Person():

    def __init__(self):
        self.first_name = None
        self.second_name = None
        self.official=True

    def print_my_name(self):
        print("My name is ", self.first_name, self.second_name)

    def greet_inoffically(self):
        print("Hallo", self.first_name)

    def greet_offically(self):
        print("Sehr geehrte Frau/Sehr geehrter Herr", self.second_name)

    def greet(self):
        if self.official:
            self.greet_offically()
        else:
            self.greet_inoffically()