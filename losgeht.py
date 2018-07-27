from math import sqrt

import Person
from Restaurants import Restaurant



me=Person.Person()
me.first_name="Ceyda"
me.second_name="Günes"

me.print_my_name()

user2=Person.Person()
user2.first_name="Erdem"
user2.second_name="Cimenoglu"
user2.print_my_name()

user3=Person.Person()
user3.first_name="Enes"
user3.second_name="Akay"
user3.official =False

user2.greet()
user3.greet()

all_restaurants = []

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


def distance(point_1, point_2):

    distance = sqrt((point_1[0] - point_2[0]) ** 2 +
                    (point_1[1] - point_2[1]) ** 2 )

    return distance


if __name__ == """__main__""":
    main()

