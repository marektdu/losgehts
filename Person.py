class Person():

    def __init__(self):
        self.first_name = None
        self.second_name = None
        self.official=True

    def print_my_name(self):
        print("My name is ", self.first_name, self.second_name)

    def greet_inoffically(self):
        return "Hallo " + self.first_name

    def greet_offically(self):
        return "Sehr geehrte Frau/Sehr geehrter Herr " + self.second_name

    def greet(self):
        greetings = None
        if self.official:
            greetings = self.greet_offically()
        else:
            greetings = self.greet_inoffically()

        print(greetings)

        return greetings