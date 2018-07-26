import unittest
import Person


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
        print (user3)
        greet_value = user3.greet()

        self.assertEqual (greet_value[0:5] ,"Hallo" )


class TestRestaurantFinder(unittest.TestCase):

    def test_something(self):

        self.assertTrue(False)



if __name__ == '''__main__''':
    unittest.main()