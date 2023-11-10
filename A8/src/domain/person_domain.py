class Person:
    def __init__(self, person_id, name, phone_number):
        self.person_id = person_id
        self.name = name
        self.phone_number = phone_number

    def get_person_id(self):
        return self.person_id

    def get_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def __eq__(self, other):
        return self.person_id == other.person_id

    def __str__(self):
        return "\nPerson: \n ID: {} \n Name: {} \n Phone #: {}".format(self.person_id, self.name, self.phone_number)

    def __repr__(self):
        return self.__str__()
