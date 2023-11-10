
import copy


def new_flight(code: str, duration: str, departure_city: str, destination_city: str):
    """
    return a list of these
    :param code:
    :param duration:
    :param departure_city:
    :param destination_city:
    :return:
    """
    return [code, duration, departure_city, destination_city]


def hardcode_flights():
    """
    hard codes some flights
    :return:
    """
    flight_list = [['1C123', '50', 'Sibiu', 'Bucuresti'], ['2X145', '60', 'Salaj', 'Cluj-Napoca'],
                   ['5Y155', '100', 'Satu Mare', 'Oradea'], ['2X56512S', '120', 'Iasi', 'Timisoara'], ['42552A', '35', 'Alba', 'Arad'],
                   ['4161X', '80', 'Frankfurt', 'Londra'], ['41QX', '130', 'Rasinari', 'Budapesta']]
    return flight_list


def add_flight(flight_list: list, code: str, duration: str, departure_city: str, destination_city: str):
    """
    adds a flight
    :param flight_list:
    :param code:
    :param duration:
    :param departure_city:
    :param destination_city:
    :return:
    """
    if len(code) < 3:
        raise ValueError("The length of the code is less than 3, flight not registered. \n")
    elif duration.isdigit() is False or int(duration) < 20:
        raise ValueError("The duration is not valid, flight not registered. \n")
    elif len(departure_city) < 3 and departure_city.isdigit() is False:
        raise ValueError("The length of the departure city is less than 3, flight not registered. \n")
    elif len(destination_city) < 3 and destination_city.isdigit() is False:
        raise ValueError("The length of the destination city is less than 3, flight not registered. \n")

    if new_flight(code, duration, departure_city, destination_city) not in flight_list:
        flight_list.append(new_flight(code, duration, departure_city, destination_city))
    else:
        raise ValueError("The flight is already registered")


def find_flight_index_code(flight_list: list, code: str):
    """
    finds the index of the flight with this code
    :param flight_list:
    :param code:
    :return:
    """
    for index in range(len(flight_list)):
        if code == flight_list[index][0]:
            return index
    raise ValueError("The code was not found.")


def delete_flight(flight_list, code: str):
    """
    if it exists, it deletes a flight
    :param flight_list:
    :param code:
    :return:
    """
    index = find_flight_index_code(flight_list, code)
    flight_list.pop(index)
    return 1


def to_str(flight: list):
    """
    makes it easier to see on listing
    :param flight:
    :return:
    """
    return 'Code: ' + str(flight[0]) + ' Duration: ' + str(flight[1]) + ' Departure City: ' + str(flight[2]) + ' Destination City: ' + str(flight[3])


def list_flight_list(flight_list: list):
    """
    list all flights
    :param flight_list:
    :return:
    """
    sorted_list = flight_list[:]
    sorted_list.sort()
    return "CURRENT FLIGHTS:\n" + "\n".join(map(to_str, sorted_list))


def list_flight_with_departure_city(flight_list: list, departure_city: str):
    """
    for point 3.
    :param flight_list:
    :param departure_city:
    :return:
    """
    flight_list_with_departure_city = []
    flag = 0
    for i in range(len(flight_list)):
        if flight_list[i][2] == departure_city:
            flight_list_with_departure_city.append(flight_list[i])
            flag = 1
    if flag == 1:
        for i in range(len(flight_list_with_departure_city) - 1):
            for j in range(i, len(flight_list_with_departure_city)):
                if flight_list_with_departure_city[i][3] > flight_list_with_departure_city[j][3]:
                    aux_flight = copy.deepcopy(flight_list_with_departure_city[i])
                    flight_list_with_departure_city[i] = copy.deepcopy(flight_list_with_departure_city[j])
                    flight_list_with_departure_city[j] = copy.deepcopy(aux_flight)
        return "CURRENT FLIGHTS:\n" + "\n".join(map(to_str, flight_list_with_departure_city))
    else:
        raise ValueError("There are no such departure cities \n")


def wind(flight_list: list, departure_city: str, minutes: str):
    """
    for point 4.
    :param flight_list:
    :param departure_city:
    :param minutes:
    :return:
    """
    flag = 0
    if 10 <= int(minutes) <= 60:
        for i in range(len(flight_list)):
            if flight_list[i][2] == departure_city:
                flight_list[i][1] = str(int(flight_list[i][1]) + int(minutes))
                flag = 1
        if flag == 0:
            raise ValueError("There are no such departure cities \n")
    else:
        raise ValueError("The minutes are not within range \n")


def test():
    flight_list = hardcode_flights()
    code = '1C123'
    assert delete_flight(flight_list, code) == 1
    code = '41QX'
    assert delete_flight(flight_list, code) == 1
    