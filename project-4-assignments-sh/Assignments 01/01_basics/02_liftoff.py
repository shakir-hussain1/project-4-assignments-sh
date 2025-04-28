# This program prints a countdown from 10 to 1, followed by "Liftoff!" to simulate a spaceship launch.

def main():
    print("Countdown to start!")
    for i in range(10 , 0 , -1):
        print(i)
    print("Liftoff!")

if __name__ == "__main__":
    main()
