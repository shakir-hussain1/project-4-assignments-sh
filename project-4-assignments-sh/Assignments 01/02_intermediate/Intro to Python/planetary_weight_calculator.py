# This program calculates and prints the equivalent weight of a user on a chosen planet based on their weight on Earth.

# Gravitational constants for each planet
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():

    earth_weight = float(input("Enter a weight on Earth: "))

    planet_choice = input("Enter a planet: ")

    if planet_choice == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet_choice == "Venus":
        gravity = VENUS_GRAVITY
    elif planet_choice == "Mars":
        gravity = MARS_GRAVITY
    elif planet_choice == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet_choice == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet_choice == "Uranus":
        gravity = URANUS_GRAVITY
    elif planet_choice == "Neptune":
        gravity = NEPTUNE_GRAVITY
    else:
        print("Invalid planet choice. Please enter a valid planet name.")
        return

    planet_weight = earth_weight * gravity
    rounded_weight = round(planet_weight, 2)

    print("The equivalent weight on " + planet_choice + ":  " + str(rounded_weight))

if __name__ == "__main__":
    main()

