class Person():


    def __init__(self, first_name=None,second_name=None,x_coord=None,y_coord=None):

        self.first_name = first_name
        self.second_name = second_name
        self.official=True

        self.x_coord = x_coord
        self.y_coord = y_coord

# some comment



    def get_coord(self):

        return (self.x_coord , self.y_coord )

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

