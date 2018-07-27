from math import sqrt

import Person


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


def distance(point_1, point_2):

    distance = sqrt((point_1[0] - point_2[0]) ** 2 +
                    (point_1[1] - point_2[1]) ** 2 )
    return distance


sayac=0
for point_2 in resturantlistesi.kordinat :
    distance[sayac] = distance(personalkordinat , point_2)



def bubble(badlist):
    length = len(badlist-1)
    unsorted = False

    while not unsorted:
        unsorted = True
        for element in range(0 , length):
            if badlist[element] > badlist[element - 1]:
                unsorted = False
                hold = badlist[element + 1]
                badlist[element + 1] = badlist[element]
                badlist[element] = hold

    return badlist

RankedList = bubble(distance)

def ShowResturant(List):
    length = len(List-1)

    for sayac in range(0, length):
        for sayac2 in range(0,length):
            if RankedList(sayac) == distance[sayac2]:
                ShowresturantList[sayac] = Resturant[sayac2]
    return ShowResturantList

ShowResturantList = ShowResturant(RankedList)