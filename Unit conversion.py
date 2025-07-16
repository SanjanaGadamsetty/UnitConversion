#PROGRAM TO CONVERT UNITS OF LENGTH,MASS AND TEMPERATURE:-

#Length conversion def
def length_converter(value, from_unit, to_unit):
    length_units = {'meters': 1,'kilometers': 1000,'centimeters': 0.01,'millimeters': 0.001,'inches': 0.0254,'feet': 0.3048,'yards': 0.9144,'miles': 1609.34}
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[from_unit] / length_units[to_unit])
    else:
        return "Invalid length units"

#Mass conversion def
def mass_converter(value, from_unit, to_unit):
    mass_units = {'kilograms': 1,'grams': 0.001,'milligrams': 0.000001,'pounds': 0.453592,'ounces': 0.0283495}
    if from_unit in mass_units and to_unit in mass_units:
        return value * (mass_units[from_unit] / mass_units[to_unit])
    else:
        return "Invalid mass units"

#Temperature conversion def
def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid temperature units"

#Function call function
def unit_converter():
    print("Choose the type of conversion:\n1. Length\n2. Mass\n3. Temperature")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        value = float(input("Enter the length value: "))
        from_unit = input("Enter the from unit (meters, kilometers, centimeters, millimeters, inches, feet, yards, miles): ").lower()
        to_unit = input("Enter the to unit (meters, kilometers, centimeters, millimeters, inches, feet, yards, miles): ").lower()
        result = length_converter(value, from_unit, to_unit)
        print(f"Converted value: {result} {to_unit}")
    
    elif choice == '2':
        value = float(input("Enter the mass value: "))
        from_unit = input("Enter the from unit (kilograms, grams, milligrams, pounds, ounces): ").lower()
        to_unit = input("Enter the to unit (kilograms, grams, milligrams, pounds, ounces): ").lower()
        result = mass_converter(value, from_unit, to_unit)
        print(f"Converted value: {result} {to_unit}")
    
    elif choice == '3':
        value = float(input("Enter the temperature value: "))
        from_unit = input("Enter the from unit (Celsius, Fahrenheit, Kelvin): ").capitalize()
        to_unit = input("Enter the to unit (Celsius, Fahrenheit, Kelvin): ").capitalize()
        result = temperature_converter(value, from_unit, to_unit)
        print(f"Converted value: {result} {to_unit}")
    
    else:
        print("Invalid choice!")

#Main Function Call
unit_converter()
