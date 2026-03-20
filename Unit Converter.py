def length_converter():
    print("\nLength Converter")
    print("1. KM to Miles")
    print("2. Miles to KM")
    print("3. Meters to CM")
    print("4. CM to Meters")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))
    
    if choice == 1:
        print("Result:", value * 0.621371, "miles")
    elif choice == 2:
        print("Result:", value * 1.60934, "km")
    elif choice == 3:
        print("Result:", value * 100, "cm")
    elif choice == 4:
        print("Result:", value / 100, "meters")
    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. KG to Pounds")
    print("2. Pounds to KG")
    print("3. Grams to KG")
    print("4. KG to Grams")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))
    
    if choice == 1:
        print("Result:", value * 2.20462, "pounds")
    elif choice == 2:
        print("Result:", value * 0.453592, "kg")
    elif choice == 3:
        print("Result:", value / 1000, "kg")
    elif choice == 4:
        print("Result:", value * 1000, "grams")
    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))
    
    if choice == 1:
        print("Result:", (value * 9/5) + 32, "°F")
    elif choice == 2:
        print("Result:", (value - 32) * 5/9, "°C")
    elif choice == 3:
        print("Result:", value + 273.15, "K")
    elif choice == 4:
        print("Result:", value - 273.15, "°C")
    else:
        print("Invalid choice")


while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    
    choice = int(input("Choose option: "))
    
    if choice == 1:
        length_converter()
    elif choice == 2:
        weight_converter()
    elif choice == 3:
        temperature_converter()
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice")