import unittest

from src.domain.person_domain import Person
from src.repository.person_repository import PersonRepository


class PersonService:
    def __init__(self, person_repository):
        self.__person_repository = person_repository

    def add_person(self, person_id, name, phone_number):
        person = Person(person_id, name, phone_number)
        self.__person_repository.add(person)

    def remove_person(self, person_id):
        self.__person_repository.remove(person_id)

    def update_person(self, person_id, new_name, new_phone_number):
        self.__person_repository.update(person_id, new_name, new_phone_number)

    def get_all_persons(self):
        return self.__person_repository.get_all()

    def get_person_by_id(self, person_id):
        return self.__person_repository.get_person_by_id(person_id)

    def search_persons(self, search: str):
        persons = self.__person_repository.get_all()
        persons_found = []
        for person in persons:
            if search.lower() in person.name.lower():
                persons_found.append(person)
            elif search.lower() in person.phone_number.lower():
                persons_found.append(person)
        return persons_found

    def activities_with_person(self, person, activities: list):
        string = ""
        persons_found = self.search_persons(person)
        for i in range(len(persons_found)):
            string += str(self.get_person_by_id(persons_found[i]))
            for activity in activities:
                if persons_found[i] in activity.get_person_id():
                    string += str(activity)
        return string


class TestPersonService(unittest.TestCase):
    def test_add_person(self):
        person = Person(1, "John", "123456789")
        person_repository = PersonRepository()
        person_service = PersonService(person_repository)
        self.assertEqual(person_service.get_all_persons(), [])
        person_service.add_person(1, "John", "123456789")
        self.assertEqual(person_service.get_all_persons(), [person])

    def test_remove_person(self):
        person = Person(1, "John", "123456789")
        person_repository = PersonRepository()
        person_service = PersonService(person_repository)
        person_service.add_person(1, "John", "123456789")
        self.assertEqual(person_service.get_all_persons(), [person])
        person_service.remove_person(1)
        self.assertEqual(person_service.get_all_persons(), [])

    def test_update_person(self):
        person = Person(1, "John", "123456789")
        person_repository = PersonRepository()
        person_service = PersonService(person_repository)
        person_service.add_person(1, "John", "123456789")
        self.assertEqual(person_service.get_all_persons(), [person])
        person_service.update_person(1, "John", "987654321")
        self.assertEqual(person_service.get_all_persons(), [Person(1, "John", "987654321")])

    def test_get_all_persons(self):
        person = Person(1, "John", "123456789")
        person_repository = PersonRepository()
        person_service = PersonService(person_repository)
        person_service.add_person(1, "John", "123456789")
        self.assertEqual(person_service.get_all_persons(), [person])

    def test_get_person_by_id(self):
        person = Person(1, "John", "123456789")
        person_repository = PersonRepository()
        person_service = PersonService(person_repository)
        person_service.add_person(1, "John", "123456789")
        self.assertEqual(person_service.get_person_by_id(1), person)

    def test_search_persons(self):
        person = Person(1, "John", "123456789")
        person_repository = PersonRepository()
        person_service = PersonService(person_repository)
        person_service.add_person(1, "John", "123456789")
        self.assertEqual(person_service.search_persons("John"), [person])


if __name__ == '__main__':
    unittest.main()

