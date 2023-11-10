class PersonRepository:
    def __init__(self):
        self.__persons = []

    def add(self, person):
        self.__persons.append(person)

    def get_all(self):
        return self.__persons

    def get_person_by_id(self, person_id):
        for person in self.__persons:
            if person.person_id == person_id:
                return person

    def remove(self, person_id):
        for person in self.__persons:
            if person.person_id == person_id:
                self.__persons.remove(person)

    def update(self, person_id, new_name, new_phone_number):
        for person in self.__persons:
            if person.person_id == person_id:
                person.name = new_name
                person.phone_number = new_phone_number

    def __str__(self):
        return "PersonRepository: {}".format(self.__persons)

    def __repr__(self):
        return self.__str__()
