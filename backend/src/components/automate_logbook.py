import subprocess
import getpass
import os
import csv 


def automate_logbook():
    """
    Utilises Boardlib base retrieval calling on climbing board APIs [credit to @lemeryfertitta]
    for logbook recorded data. User's logbook data is inputted into boardlib and returned as a 
    csv file for later manipulation.

    Time Complexity: 
        - Best: O(1 + T(sbp) + n + m)
        - Worst: O(1 + T(sbp) + n + m)
        where n is the number of rows and m is the number of entries fetched
    """
    #Map of valid boards and the corresponding databases for access
    boardDatabasePath = {
        "kilter": "databases/kilter.db",  
        "tension": "databases/tension.db", 
        "touchstone": "databases/touchstone.db", 
        "aurora": "databases/aurora.db",  
        "decoy": "databases/decoy.db" 
    }

    #Retrieve user input on desired board utilised and corresponding username
    while True:
        board = input("Select board [kilter, tension, touchstone, aurora, decoy]: ").lower()
        
        #Check if board is valid 
        if board in boardDatabasePath:
            break 
        else:
            print("Invalid input please select one of the available boards [kilter, tension, touchstone, aurora, decoy]")


    username = input("Enter your username: ")

    databasePath = boardDatabasePath[board]

    localFile = "logbook.csv"
    tempFile = "temp_logbook.csv"

    #Boardlib shell output line
    inputCom = [
        "boardlib", "logbook", 
        "--username", username,
        "--output", tempFile,
        "--grade-type", "hueco",  
        "--database", databasePath,
        board 
    ]

    #Simulate the input line with subprocess
    #Error checking for testing 
    try:
        subprocess.run(inputCom, check=True)
        # Load existing local entries
        local_entries = load_csv(localFile)

        # Load fetched entries
        fetched_entries = load_csv(tempFile)

        # Merge entries
        merged_entries = merge_logbooks(local_entries, fetched_entries)

        # Save merged entries back to the local logbook
        save_csv(localFile, merged_entries)

        #print out table 
        print(f"{'Board':<10} {'Angle':<10} {'Climb Name':<25} {'Date':<20} {'Logged Grade':<15} {'Displayed Grade':<15} {'Difficulty':<15} {'Is Benchmark':<15} {'Tries':<10}")
        print("-" * 140)

        with open(localFile, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['board']:<10} {row['angle']:<10} {row['climb_name']:<25} {row['date']:<20} {row['logged_grade']:<15} {row['displayed_grade']:<15} {row['difficulty']:<15} {row['is_benchmark']:<15} {row['tries']:<10}")

    except subprocess.CalledProcessError as e:
        print(f"An error has occured: {e}")
    

def load_csv(file_path):
    """
    Load entries from a CSV file.

    Time Complexity: 
        - Best: O(n)
        - Worst: O(n)
        where n is the number of rows 
    """
    entries = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            entries = [row for row in reader]
    except FileNotFoundError:

        # Return an empty list if the file doesn't exist
        print(f"{file_path} not found. Starting a new logbook.")
    return entries


def merge_logbooks(local_entries, fetched_entries):
    """
    Merge local and fetched entries, avoiding duplicates and ensuring both local entries are updated to the stored logbook.

    Time Complexity: 
        - Best: O(p + q)
        - Worst: O(p + q)
        p is number of local entries and q is the number of fetched entries
    """
    exisitingKeys = set((entry['board'], entry['angle'], entry['climb_name'], entry['date']) for entry in local_entries)

    for entry in fetched_entries:

        key = (entry['board'], entry['angle'], entry['climb_name'], entry['date'])
        if key not in exisitingKeys:
            local_entries.append(entry) 

    return local_entries


def save_csv(file_path, entries):
    """
    Save entries to a CSV file.

    Time Complexity: 
        - Best: O(r * k)
        - Worst: O(r * k)
        where r is the number of rows and k is the number of sets
    """
    if not entries:
        print("No entries to save.")
        return

    fieldNames = entries[0].keys()
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(entries)

