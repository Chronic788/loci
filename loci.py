
# This is Loci
# ------------------------------------------------------------------------------
# Loci is meant to boost focus and productivity at work and at home.
# It asks key questions about your day to help you record what is important and
# keep your work moving.
# ------------------------------------------------------------------------------

import datetime
import os
import platform

linuxBasePath = "/home/jared/Desktop/logs"
windowsBasePath = "C:\\Common\\"

linuxWorkLogPath = "/work_logs/"
windowsWorkLogPath = "\\work_logs\\"

newLine = "\n"
twoNewLines = "\n\n"
smallDivider = "----------------"
mediumDivider = "------------------------------"
largeDivider = "---------------------------------------------"

def writeFile(logTypePath, fileName, contents):

    # Make final path
    finalPath = linuxBasePath + logTypePath
    if(platform.system() == 'Windows'):
        finalPath = windowsBasePath + windowsWorkLogPath
            

    # Check if path exists
    if not os.path.exists(finalPath):
        os.makedirs(finalPath)

    # Write contents of file
    fileName = fileName.replace(":", ".")
    filePath = finalPath + fileName + ".txt"
    entryFile = open(filePath, "w")
    entryFile.write(contents)
    entryFile.close()

# Makes a 110 character-wide paragraph from the given text
def makeParagraph(text):

    finalText = ""
    textWords = text.split(" ")
    charCount = 0
    for textWord in textWords:
        if not len(textWord) + charCount < 110:
            finalText = finalText + "\n"
            charCount = 0
        charCount = charCount + len(textWord)
        finalText = finalText + textWord + " "

    return finalText

def logWorkEntry():

    # Form the title for the work log
    date = datetime.datetime.now()
    # Weekday - Month - Day of Month - Year
    workLogEntryTitle = date.strftime("%a %b %d, %Y")

    # Start the outstring
    outString = "Work Log Entry" + newLine

    # Start the entry
    print(newLine + mediumDivider)
    print(workLogEntryTitle + " Work Log Entry")
    print(mediumDivider)

    # Record the date and time
    outString = outString + smallDivider + newLine
    dateAndTime = date.strftime("%a %b %d, %Y - %I:%M %p") + " Work Log"
    outString = outString + dateAndTime
    outString = outString + newLine + mediumDivider + newLine

    # Accomplishments
    accomplishments = input("\nWhat were some of your accomplishments today?\n\n")
    accomplishments = makeParagraph(accomplishments)
    outString = outString + newLine + "Accomplishments" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + accomplishments) + twoNewLines

    # Difficulties
    difficulties = input("\nWhat were some of the difficulties you faced today?\n\n")
    difficulties = makeParagraph(difficulties)
    outString = outString + newLine + "Difficulties" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + difficulties) + twoNewLines

    # Notes
    notes = input("\nEnter some notes about work today:\n\n")
    notes = makeParagraph(notes)
    outString = outString + newLine + "Notes" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + notes) + twoNewLines

    # Productivity score
    productivity = input("\nWhat was your productivity level (from 1 to 10)?\n\n")
    outString = outString + newLine + "Productivity Score" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + productivity) + twoNewLines

    # What are you doing tomorrow
    doingTomorrow = input("\nWhat are you doing tomorrow?\n\n")
    outString = outString + newLine + "What you are doing tomorrow" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + doingTomorrow) + twoNewLines

    # Write the file
    writeFile(linuxWorkLogPath, dateAndTime, outString)

    # Confirm
    print(newLine + "Work successfully logged!")

# Main function call
logWorkEntry()