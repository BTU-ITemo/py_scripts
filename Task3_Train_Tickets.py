data = {
    1: [
        { "seat_name": "a1", "isTaken": True },
        { "seat_name": "a2", "isTaken": False },
        { "seat_name": "a3", "isTaken": True },
        { "seat_name": "a4", "isTaken": True },
        { "seat_name": "a5", "isTaken": False },
    ],
    2: [
        { "seat_name": "b1", "isTaken": False },
        { "seat_name": "b2", "isTaken": False },
        { "seat_name": "b3", "isTaken": True },
        { "seat_name": "b4", "isTaken": False },
        { "seat_name": "b5", "isTaken": True },
    ],
    3: [
        { "seat_name": "c1", "isTaken": False },
        { "seat_name": "c2", "isTaken": True },
        { "seat_name": "c3", "isTaken": True },
        { "seat_name": "c4", "isTaken": True },
        { "seat_name": "c5", "isTaken": False },
    ],
}

def find_seat():
    carriage_number = int(input("Enter the carriage number: "))
    seat_name = input("Enter the seat name (e.g. a1, b3, c5): ")
    
    carriage_data = data.get(carriage_number)
    if carriage_data:
        for seat_data in carriage_data:
            if seat_data["seat_name"] == seat_name:
                if seat_data["isTaken"]:
                    print(f"Seat {seat_name} is taken. Checking for the nearest seat...")
                    # Check if any seat adjacent to the selected seat is free
                    index = carriage_data.index(seat_data)
                    if index > 0 and not carriage_data[index-1]["isTaken"]:
                        print(f"Seat {seat_data['seat_name']} is taken. The nearest available seat is {carriage_data[index-1]['seat_name']}.")
                        return
                    elif index < len(carriage_data)-1 and not carriage_data[index+1]["isTaken"]:
                        print(f"Seat {seat_data['seat_name']} is taken. The nearest available seat is {carriage_data[index+1]['seat_name']}.")
                        return
                    else:
                        print("There is no available seat adjacent to the selected seat.")
                        break
                else:
                    print(f"Seat {seat_name} is available.")
                    return
        else:
            print(f"Seat {seat_name} does not exist in carriage {carriage_number}.")
    else:
        print(f"Carriage {carriage_number} does not exist!")

# Start of the program
find_seat()