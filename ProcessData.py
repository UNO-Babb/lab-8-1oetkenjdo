#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def processLine(line):
    """Processes a single line from the input file and returns a formatted CSV line."""
    firstName, lastName, email, stdID, bday, year, major = line.strip().split(maxsplit=6)


    if len(lastName) < 5:
        lastName += "x" * (5 - len(lastName))


    userID = f"{firstName[0].lower()}{lastName.lower()}{stdID[-4:]}"  


    yearAbbreviation = {
        "Freshman": "FR",
        "Sophomore": "SO",
        "Junior": "JR",
        "Senior": "SR"
    }
    majorYear = f"{major[:3].upper()}-{yearAbbreviation.get(year, 'UNK')}"

    return f"{lastName},{firstName},{userID},{majorYear}\n"


def main():
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')
    outFile.write("Last Name,First Name,User ID,Major-Year\n")
    for line in inFile:
        formattedLine = processLine(line)
        outFile.write(formattedLine)

    inFile.close()
    outFile.close()

if __name__ == '__main__':
    main()