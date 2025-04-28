# This program converts Fahrenheit to Celsius

def main():
    print("Fahrenheit to Celsius Converter")
    fahrenheit :str = float(input("Enter  temperature in Fahrenheit :"))

    # Convert Fahrenheit to Celsius
    celsius :float =  (fahrenheit - 32) * 5.0/9.0

    # Display the result
    print(f"Temperature :{fahrenheit:.1f}F = {celsius:}C")

    # Python file to call the main() function.
if __name__ == '__main__':
    main()
