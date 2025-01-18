
def log():
    """
    Allows users to manually log a climb with details like grade, date and additional comments if required. 
    This is done to allow climbers to log climbs that aren't benchmarked and unique to the user's local
    climbing gym.

    Time Complexity: 
        - Best:
        - Worst: 
    """
    #Utilises Boardlib csv file for based inputs, basic modfied for standard climbing and defaults are preset
    
    board = input("Enter the board name: ")
    angle = "Null"
    climbName = input("Enter the climb name [e.g gym colour climb]: ")
    date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
    logGrade = input("Enter the grade (e.g V5): ")
    displayGrade = logGrade
    difficulty = "Null"
    isBench = "False"
    tries = input("Enter the number of tries: ")
    isMirror = "False" 
    sessionCount = input("Enter the number of sessions taken: ")
    triesTotal = tries 
    isRepeat = "False"  
    isAscent = "True"  
    comment = input("Add any additional notes: ")

    # Append the new entry to the CSV file
    with open("logbook.csv", "a") as file:
        file.write(
            f"{board},{angle},{climbName},{date},{logGrade},{displayGrade},"
            f"{difficulty},{isBench},{tries},{isMirror},{sessionCount},"
            f"{triesTotal},{isRepeat},{isAscent},{comment}\n"
        )

    print("Climb successfully logged!")