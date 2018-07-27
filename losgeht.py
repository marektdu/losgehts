from math import sqrt

import Person
from Restaurants import Restaurant




all_personen = []
all_restaurants = []

def define_personen():

    global all_personen

    all_personen.append(Person(first_name="Ceyda", second_name="Günes", x_coord=10., y_coord=12., range=2000))
#user2 = Person.Person(first_name="Erdem", second_name="Cimenoglu", x_coord=12., y_coord=13., range=3000)
#user3 = Person.Person(first_name="Enes", second_name="Akay", x_coord=15., y_coord=20., range=1500)



def define_restaurants():

    global all_restaurants

    all_restaurants.append(Restaurant(name="Pizzaria", coordinates=(11, 12), openinghours=None, freeSeats=100))
    all_restaurants.append(Restaurant(name="Pizzaria2", coordinates=(10, 113), openinghours=None, freeSeats=150))





def print_all_restaurant_information( restaurant_list):

    for rr in restaurant_list:
        print (rr)



def main():

    #load all data
    define_restaurants()

    print_all_restaurant_information(all_restaurants)

    print_all_personen_information()

def distance(point_1, point_2):

    distance = sqrt((point_1[0] - point_2[0]) ** 2 +
                    (point_1[1] - point_2[1]) ** 2 )

    return distance


if __name__ == """__main__""":
    main()

