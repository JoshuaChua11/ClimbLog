import datetime
import math
import csv

def roi():
    """
    Analyses the data from our logbook utilising a numerical logerithmic assignment to each respective grade.
    Currently this numerical value is purely assigned by representation and the exponential nature of grades, 
    however through further data analysis or other methods a more reasonable approach can be determined. 

    Time Complexity: 
    - 
    - 
    """
    logbookFile = "logbook.csv"

    gradesDifficulty = {
        "V0": 1, "V1": 2, "V2": 4, "V3": 8, "V4": 16, "V5": 32,
        "V6": 64, "V7": 128, "V8": 256, "V9": 512, "V10": 1024,
        "V11": 2048, "V12": 4096, "V13": 8192, "V14": 16384
    }

    #Load all entries
    try:
        with open(logbookFile, mode='r') as file:
            reader = csv.DictReader(file)
            log_entries = [row for row in reader]

    except FileNotFoundError:
        print(f"Logbook file '{logbookFile}' not found.")
        return

    if not log_entries:
        print("Logbook is empty. Please log climbs before tracking improvement.")
        return

    #Extract date and grade
    climbs = []
    for entry in log_entries:
        try:
            date = datetime.datetime.strptime(entry['date'], "%Y-%m-%d %H:%M:%S")
            grade = entry['logged_grade']

            #append grades climbs 
            if grade in gradesDifficulty:
                climbs.append((date, grade))
        except (KeyError, ValueError):
            continue

    #Sort climbs by date
    climbs.sort(key=lambda x: x[0])

    #Compute improvement over time
    gradeDates = {}
    for date, grade in climbs:
        if grade not in gradeDates:
            gradeDates[grade] = date

    #base case for low entries  
    sortGrades = sorted(gradeDates.keys(), key=lambda g: gradesDifficulty[g])
    if len(sortGrades) < 2:
        print("Not enough grade progression data to analyze improvement.")
        return

    #Grab deltas between each grade gap and append 
    gradeDeltas = []
    for i in range(1, len(sortGrades)):
        currentGrade = sortGrades[i - 1]
        nextGrade = sortGrades[i]
        timeDiff = (gradeDates[nextGrade] - gradeDates[currentGrade]).days
        gradeDeltas.append((currentGrade, nextGrade, timeDiff))

    #last grades is the last highest grade recorded
    lastGade = sortGrades[-1]

    currDifficulty = gradesDifficulty[lastGade]
    nextGradeDiff = currDifficulty * 2
    nextGrade = None

    for grade, difficulty in gradesDifficulty.items():
        if difficulty == nextGradeDiff:
            nextGrade = grade
            break

    if not nextGrade:
        print("Congratulations! You've reached the highest grade in our records.")
        return

    #Estimate time to each the next grade 
    if gradeDeltas:
        avgTime = sum(delta[2] / gradesDifficulty[delta[1]] for delta in gradeDeltas) / len(gradeDeltas)
        predDays = math.ceil(avgTime * nextGradeDiff)

        print(f"Current Grade: {currentGrade}")
        print(f"Next Target Grade: {nextGrade}")
        print(f"Estimated Time to Reach {nextGrade}: {predDays} days")
    else:
        print("Not enough data to predict improvement timeline.")