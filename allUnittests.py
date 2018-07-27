import unittest
from Person import Person

from Restaurants import Restaurant

class TestGreetingMethods(unittest.TestCase):

    def test_offically(self):

        user2=Person(first_name="Erdem", second_name="Cimenoglu")
        greet_value = user2.greet()

        self.assertEqual(greet_value[0:9], "Sehr geeh")

    def test_inoffically(self):

        user3=Person(first_name="Enes", second_name="Akay")
        user3.official =False

        greet_value = user3.greet()

        self.assertEqual (greet_value[0:5] ,"Hallo" )


class TestRestaurantFinder(unittest.TestCase):

    def test_something(self):

        self.assertTrue(False)



    def test_getCoord(self):
        p = Person('Tom','Tomas', 12., 25.)

        self.assertEqual(p.x_coord, 12.)
        self.assertEqual(p.y_coord, 25.)


class TestRestaurant(unittest.TestCase):

    def test_something(self):
        myRestaurant = Restaurant("Pizzaria", (11, 12), (12.00, 22.00), 100)
        print(myRestaurant)

        self.assertEqual(myRestaurant.freeSeats, 100)

if __name__ == '''__main__''':
    unittest.main()