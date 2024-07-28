# Had this idea for when I was in Canada

def mph_to_kmh(mph):
    return round(mph * 1.60934)

def kmh_to_mph(kmh):
    return round(kmh / 1.60934)

def main():
    while True:
        print("Choose conversion type:")
        print("1. MPH to KMH")
        print("2. KMH to MPH")
        print("3. Exit")

        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            mph = int(input("Enter speed in MPH (whole number): "))
            kmh = mph_to_kmh(mph)
            print(f"{mph} MPH is {kmh} KMH\n")
        elif choice == '2':
            kmh = int(input("Enter speed in KMH (whole number): "))
            mph = kmh_to_mph(kmh)
            print(f"{kmh} KMH is {mph} MPH\n")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
