import math

def calc(mass: int) -> int:
    return math.floor(mass / 3) - 2

def calc_with_fuel(initial_mass: int) -> int:
    result = 0
    required_fuel_to_transport_fuel = calc(initial_mass)

    while required_fuel_to_transport_fuel > 0:
        result += required_fuel_to_transport_fuel
        required_fuel = required_fuel_to_transport_fuel
        required_fuel_to_transport_fuel = calc(required_fuel)

    return result

def main():
    input_data = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            input_data.append(int(line))
            line = fp.readline()

    required_fuel_for_cargo = 0
    for input_entry in input_data:
        required_fuel_for_cargo += calc(input_entry)

    print('First part answer: %s' % required_fuel_for_cargo)

    required_fuel_for_cargo_with_fuel = 0
    for input_entry in input_data:
        required_fuel_for_cargo_with_fuel += calc_with_fuel(input_entry)

    print('Second part answer: %s' % required_fuel_for_cargo_with_fuel)

if __name__ == '__main__':
    main()