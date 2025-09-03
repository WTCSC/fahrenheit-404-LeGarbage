def parse_temperature(temperature):
    if temperature.lower() in "fahrenheit":
        return "fahrenheit"
    if temperature.lower() in "celsius":
        return "celsius"
    if temperature.lower() in "kelvin":
        return "kelvin"

    return ""


def parse_temperature_value(temperature):
    temperature_value = ""
    for char in temperature:
        if char in "1234567890":
            temperature_value += char
        elif char == "." and "." not in temperature_value:
            temperature_value += char

    if temperature_value == ".":
        temperature_value = ""

    return temperature_value


while True:
    print("Welcome to the temperature converter\n")

    convert_to = ""
    while not convert_to:
        convert_to = parse_temperature(input(
            "Would you like to convert to Fahrenheit, Celsius, or Kelvin? "
        ))

        if not convert_to:
            print("Invalid input. Please try again")

    temperature_value = ""
    while not temperature_value:
        temperature_value = parse_temperature_value(input(
            "\nPlease input the temperature value you would like to convert: "
        ))

        if not temperature_value:
            print("Invalid input. Please try again")

    temperature_value = float(temperature_value)

    convert_from = ""
    while not convert_from:
        convert_from = parse_temperature(input(
            "Would you like to convert from Fahrenheit, Celsius, or Kelvin? "
        ))

        if not convert_from:
            print("Invalid input. Please try again")

    if convert_from == convert_to:
        print(f"{temperature_value}°{convert_from[0].upper()} in {
              convert_to.capitalize()} is {temperature_value}")
    elif convert_from == "fahrenheit" and convert_to == "celsius":
        print(f"{temperature_value}°F in Celsius is {
              (temperature_value - 32) / 1.8}")
    elif convert_from == "fahrenheit" and convert_to == "kelvin":
        print(f"{temperature_value}°F in Kelvin is {
              ((temperature_value - 32) / 1.8) + 273.15}")
    elif convert_from == "celsius" and convert_to == "fahrenheit":
        print(f"{temperature_value}°C in Fahrenheit is {
              (temperature_value * 1.8) + 32}")
    elif convert_from == "celsius" and convert_to == "kelvin":
        print(f"{temperature_value}°C in Kelvin is {
              temperature_value + 273.15}")
    elif convert_from == "kelvin" and convert_to == "fahrenheit":
        print(f"{temperature_value}°C in Kelvin is {
            ((temperature_value - 273.15) * 1.8) + 32}")
    elif convert_from == "kelvin" and convert_to == "celsius":
        print(f"{temperature_value}°C in Kelvin is {
            temperature_value - 273.15}")
    else:
        print("Something went wrong. Please try again")
        continue

    again = input("Do you wish to convert again? [y/N]")
    if not again or again.lower() not in "yes":
        break
