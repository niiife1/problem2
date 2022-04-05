number_cars = int(input())
all_cars = {}
all_cars_info = {}
while number_cars > 0:

            number_cars -= 1
            casr_info = input().split("|")
            mark = casr_info[0]
            total_km = int(casr_info[1])
            total_fuel = int(casr_info[2])
            all_cars[mark] = [total_km,total_fuel]

while True:
                info  = input().split(" : ")
                command = info[0]
                if command == "Stop":
                    break
                name = info[1]
                kilometer = int(info[2])

                if command == "Drive":
                    fuel = int(info[3])
                    if fuel <= all_cars[name][1]:
                        all_cars[name][0] += kilometer
                        all_cars[name][1] -= fuel
                        print(f"{name} driven for {kilometer} kilometers. {fuel} liters of fuel consumed.")
                        if all_cars[name][0] > 100000:
                            del all_cars[name]
                            print(f"Time to sell the {name}!")

                    else:
                        print("Not enough fuel to make that ride")
                    continue
                elif command == "Refuel":
                    feal_in = abs(all_cars[name][1] - 75)
                    all_cars[name][1] += kilometer
                    if all_cars[name][1] > 75:
                        all_cars[name][1] = 75
                        print(f"{name} refueled with {feal_in} liters")
                    else:
                        print(f"{name} refueled with {kilometer} liters")
                elif command == "Revert":
                    all_cars[name][0] -= kilometer
                    if all_cars[name][0] < 10000:
                        all_cars[name][0] = 10000
                    else:
                        print(f"{name} mileage decreased by {kilometer} kilometers")

for key, value in all_cars.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')