class Person():

    def __init__(self, first_name, second_name,  x_coord = None, y_coord = None , range= None ):
        self.first_name = first_name
        self.second_name = second_name
        self.official=True

        self.x_coord = x_coord
        self.y_coord = y_coord
        self.range = range



    def print_my_name(self):
        print("My name is ", self.first_name, self.second_name)

    def greet_inoffically(self):
        return "Hallo" + self.first_name

    def greet_offically(self):
        return "Sehr geehrte Frau/Sehr geehrter Herr " + self.second_name

    def greet(self):
        greeetings = None
        if self.official:
           greeetings = self.greet_offically()
        else:
            greeetings = self.greet_inoffically()

        return greeetings