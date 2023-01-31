print("Welcome to the car game!")
print("To get started, type 'help'")
command = ""
car_started = False
car_stopped = False

while True:
    command = input(">").lower()
    if command == "start":
        if car_started:
            print("The car has already been started!")
        else:
            car_started = True
            print("Car started... ready to go!")
    elif command == "stop":
        if not car_started:
            print("The car is already stopped!")
        else:
            car_started = False
            print("Cat stopped.")
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")
