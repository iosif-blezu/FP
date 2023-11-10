from src.repository.activity_repository import ActivityRepository
from src.services.activity_service import ActivityService
from src.services.person_service import PersonService
from src.repository.person_repository import PersonRepository


class UI:
    def __init__(self, person_service, activity_service):
        self.__person_service = person_service
        self.__activity_service = activity_service

    def __print_menu(self):
        print("1. Add person")
        print("2. Remove person")
        print("3. Update person")
        print("4. List all persons")
        print("5. Search persons")
        print("6. Add activity")
        print("7. Remove activity")
        print("8. Update activity")
        print("9. List all activities")
        print("10. Search activities")
        print("11. Add person to activity")
        print("12. Remove person from activity")
        print("13. List all persons with a given activity")
        print("14. List all activities with a given person")
        print("15. List all persons with a given activity on a given date")
        print("16. List all activities with a given person on a given date")
        print("x. Exit")

    def __read_command(self):
        return input("Enter command: ")

    def __add_person(self):
        person_id = int(input("Enter person ID: "))
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        self.__person_service.add_person(person_id, name, phone_number)

    def __remove_person(self):
        person_id = int(input("Enter person ID: "))
        self.__person_service.remove_person(person_id)

    def __update_person(self):
        person_id = int(input("Enter person ID: "))
        new_name = input("Enter new name: ")
        new_phone_number = input("Enter new phone number: ")
        self.__person_service.update_person(person_id, new_name, new_phone_number)

    def __list_all_persons(self):
        persons = self.__person_service.get_all_persons()
        for person in persons:
            print(person)

    def __search_persons(self):
        search = input("Enter search: ")
        persons = self.__person_service.search_persons(search)
        for person in persons:
            print(person)

    def __add_activity(self):
        activity_id = int(input("Enter activity ID: "))
        date = input("Enter date: ")
        time = input("Enter time: ")
        description = input("Enter description: ")
        self.__activity_service.add_activity(activity_id, date, time, description)

    def __remove_activity(self):
        activity_id = int(input("Enter activity ID: "))
        self.__activity_service.remove_activity(activity_id)

    def __update_activity(self):
        activity_id = int(input("Enter activity ID: "))
        new_date = input("Enter new date: ")
        new_time = input("Enter new time: ")
        new_description = input("Enter new description: ")
        self.__activity_service.update_activity(activity_id, new_date, new_time, new_description)

    def __list_all_activities(self):
        activities = self.__activity_service.get_all_activities()
        for activity in activities:
            print(activity)

    def __search_activities(self):
        search = input("Enter search: ")
        activities = self.__activity_service.search_activities(search)
        for activity in activities:
            print(activity)

    def __add_person_to_activity(self):
        person_id = int(input("Enter person ID: "))
        activity_id = int(input("Enter activity ID: "))
        self.__person_service.add_person_to_activity(person_id, activity_id)

    def __remove_person_from_activity(self):
        person_id = int(input("Enter person ID: "))
        activity_id = int(input("Enter activity ID: "))
        self.__person_service.remove_person_from_activity(person_id, activity_id)

    def __list_all_persons_with_activity(self):
        activity_id = int(input("Enter activity ID: "))
        persons = self.__person_service.get_all_persons_with_activity(activity_id)
        for person in persons:
            print(person)

    def __list_all_activities_with_person(self):
        person_id = int(input("Enter person ID: "))
        activities = self.__person_service.get_all_activities_with_person(person_id)
        for activity in activities:
            print(activity)

    def __list_all_persons_with_activity_on_date(self):
        activity_id = int(input("Enter activity ID: "))
        date = input("Enter date: ")
        persons = self.__person_service.get_all_persons_with_activity_on_date(activity_id, date)
        for person in persons:
            print(person)

    def __list_all_activities_with_person_on_date(self):
        person_id = int(input("Enter person ID: "))
        date = input("Enter date: ")
        activities = self.__person_service.get_all_activities_with_person_on_date(person_id, date)
        for activity in activities:
            print(activity)

    def start(self):
        while True:
            self.__print_menu()
            command = self.__read_command()
            if command == "1":
                self.__add_person()
            elif command == "2":
                self.__remove_person()
            elif command == "3":
                self.__update_person()
            elif command == "4":
                self.__list_all_persons()
            elif command == "5":
                self.__search_persons()
            elif command == "6":
                self.__add_activity()
            elif command == "7":
                self.__remove_activity()
            elif command == "8":
                self.__update_activity()
            elif command == "9":
                self.__list_all_activities()
            elif command == "10":
                self.__search_activities()
            elif command == "11":
                self.__add_person_to_activity()
            elif command == "12":
                self.__remove_person_from_activity()
            elif command == "13":
                self.__list_all_persons_with_activity()
            elif command == "14":
                self.__list_all_activities_with_person()
            elif command == "15":
                self.__list_all_persons_with_activity_on_date()
            elif command == "16":
                self.__list_all_activities_with_person_on_date()
            elif command == "x":
                return
            else:
                print("Invalid command!")


def main():
    person_repository = PersonRepository()
    activity_repository = ActivityRepository()
    person_service = PersonService(person_repository)
    activity_service = ActivityService(activity_repository)
    ui = UI(person_service, activity_service)
    ui.start()

main()

