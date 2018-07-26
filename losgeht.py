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
