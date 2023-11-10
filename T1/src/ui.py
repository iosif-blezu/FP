import functions as f


def start_up():
    flight_list = f.hardcode_flights()
    while True:
        print("1. Add a flight.")
        print("2. Delete a flight.")
        print("3. Show all flights.")
        print("4. Show all flights with given departure city.")
        print("5. Increase flight duration.")
        print("6. Quit.")

        choice = input()

        if choice == '1':
            print("Introduce the code:")
            code = input()
            print("Introduce the duration:")
            duration = input()
            print("Introduce the departure city:")
            departure_city = input()
            print("Introduce the destination city:")
            destination_city = input()
            print()
            try:
                f.add_flight(flight_list, code, duration, departure_city, destination_city)
                print("Flight added. \n")
            except ValueError as error:
                print(str(error))
        elif choice == '2':
            print("Introduce the code:")
            code = input()
            try:
                f.delete_flight(flight_list, code)
                print("Flight deleted. \n")
            except ValueError as error:
                print(str(error))
        elif choice == '3':
            print(f.list_flight_list(flight_list))
        elif choice == '4':
            print("Introduce the departure city:")
            departure_city = input()
            if len(departure_city) >= 3:
                try:
                    print(f.list_flight_with_departure_city(flight_list, departure_city))
                except ValueError as error:
                    print(str(error))
            else:
                print("The length of the departure city is less than 3. \n")

        elif choice == '5':
            print("Introduce the departure city:")
            departure_city = input()
            print("Introduce the minutes to be added:")
            minutes = input()
            try:
                f.wind(flight_list, departure_city, minutes)
                print("Minutes added.")
            except ValueError as error:
                print(str(error))
        elif choice == '6':
            print("Quitting.")
            return
        else:
            print("Input is not valid.\n")
            f.test()
            print("Passed")


if __name__ == '__main__':
    start_up()
