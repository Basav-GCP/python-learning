class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

first_name="XYZ"
person=Person(first_name,"ABC")
first_name="LMN"
person.last_name="PQR"
print(f" This is first name - {person.first_name} and last name is {person.last_name}")