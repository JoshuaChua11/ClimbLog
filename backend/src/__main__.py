import components

def display_menu():
    """
    Basic console backend display

        Time Complexity: 
        - Best: O(1)
        - Worst: O(1)
    """
    print("\nSelect an Operation:")
    print("1. Retrieve Logbook Entries")
    print("2. Manually Log a New Climb")
    print("3. Track Improvements")
    print("4. Get AI Recommendations")
    print("5. Exit")


def main():
    while True:
        display_menu()
        try:
            function = int(input("Enter desired function [1-5]: "))

            if function == 1:
                print("\nRetrieving logbook entries...")
                components.automate_logbook()

            elif function == 2:
                print("\nLogging a new climb...")
                components.log()

            elif function == 3:
                print("\nTracking improvements...")
                components.roi()

            elif function == 4:
                print("\nGetting AI recommendations...")
                components.recs()

            elif function == 5:
                print("Exiting the program")
                break

            else:
                print("Invalid input. Please enter a number [1-5].")

        except ValueError:
            print("Invalid input. Please enter a number [1-5].")

if __name__ == "__main__":
    main()

