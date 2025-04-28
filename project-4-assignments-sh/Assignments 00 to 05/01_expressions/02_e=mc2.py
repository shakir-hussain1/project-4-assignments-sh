# program that reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy E = m * c**2

C: int = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass:"))

    energy_in_joules:float = mass_in_kg * C**2

    print("e = m * C^2...")
    print("m =" + str(mass_in_kg) + "kg")
    print("C =" + str(C) + "m/s")

    print(str(energy_in_joules) + "Joules of energy")

if __name__ == "__main__":
    main()
    