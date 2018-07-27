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

def define_personen():

    global all_personen

    all_personen.append(Person(first_name="Ceyda", second_name="Günes", x_coord=10., y_coord=12., range=2000))
#user2 = Person.Person(first_name="Erdem", second_name="Cimenoglu", x_coord=12., y_coord=13., range=3000)
#user3 = Person.Person(first_name="Enes", second_name="Akay", x_coord=15., y_coord=20., range=1500)



def define_restaurants():

    global all_restaurants

    all_restaurants.append(Restaurant(name="Pizzaria", coordinates=(5, 12), openinghours=None, freeSeats=100))
    all_restaurants.append(Restaurant(name="Pizzaria2", coordinates=(35, 113), openinghours=None, freeSeats=80))
    all_restaurants.append(Restaurant(name="Pizzaria3", coordinates=(22, 58), openinghours=None, freeSeats=90))
    all_restaurants.append(Restaurant(name="Pizzaria4", coordinates=(17, 72), openinghours=None, freeSeats=120))
    all_restaurants.append(Restaurant(name="Pizzaria5", coordinates=(15, 65), openinghours=None, freeSeats=30))


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


def get_restaurants_in_range(all_restaurants, personal_coordinates, range):
    restaurants_in_range = []

    for rr in all_restaurants:
        distance = distance(personal_coordinates, rr.coordinates)
        if distance <= range:
            restaurants_in_range.append(rr)

    return restaurants_in_range


def main():

    #load all data
    define_restaurants()

    print_all_restaurant_information(all_restaurants)




if __name__ == """__main__""":
    main()




#############



#############




# def bubble(badlist):
#     length = len(badlist-1)
#     unsorted = False
#
#     while not unsorted:
#         unsorted = True
#         for element in range(0 , length):
#             if badlist[element] > badlist[element - 1]:
#                 unsorted = False
#                 hold = badlist[element + 1]
#                 badlist[element + 1] = badlist[element]
#                 badlist[element] = hold
#
#     return badlist
#
# RankedList = bubble(distance)
#
# def ShowResturant(List):
#     length = len(List-1)
#
#     for sayac in range(0, length):
#         for sayac2 in range(0,length):
#             if RankedList(sayac) == distance[sayac2]:
#                 ShowresturantList[sayac] = Resturant[sayac2]
#     return ShowResturantList
#
# ShowResturantList = ShowResturant(RankedList)