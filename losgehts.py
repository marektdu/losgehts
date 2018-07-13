import Person

#Person.print_my_name()
me=Person.Person()
me.first_name="Sule"
me.second_name="Calıs"

me.print_my_name()

user2=Person.Person()
user2.first_name="Erdem"
user2.second_name="Cımenoglu"

user2.print_my_name()

user3=Person.Person()
user3.first_name="Enes"
user3.second_name="Akay"
user3.offical=False

user3.greet()
user2.greet()


