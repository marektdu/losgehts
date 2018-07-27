import unittest
import Person
from Restaurants import Restaurant

class TestGreetingMethods(unittest.TestCase):

    def test_offically(self):

        user2=Person.Person()
        user2.first_name="Erdem"
        user2.second_name="Cimenoglu"
        greet_value = user2.greet()

        self.assertEqual(greet_value[0:9], "Sehr geeh")

    def test_inoffically(self):

        user3=Person.Person()
        user3.first_name="Enes"
        user3.second_name="Akay"
        user3.official =False

        greet_value = user3.greet()

        self.assertEqual (greet_value[0:5] ,"Hallo" )


#class TestRestaurantFinder(unittest.TestCase):
#
#    def test_something(self):
#
#        self.assertTrue(False)

class TestRestaurant(unittest.TestCase):

    def test_something(self):
        myRestaurant = Restaurant("Pizzaria", (11, 12), (12.00, 22.00), 100)
        print(myRestaurant)

        self.assertEqual(myRestaurant.freeSeats, 100)

if __name__ == '''__main__''':
    unittest.main()