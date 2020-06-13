
# This is Loci
# ------------------------------------------------------------------------------
# Loci is meant to boost focus and productivity at work and at home.
# It does so by providing an easy way to log work progress and also to journal.
# ------------------------------------------------------------------------------

import datetime

basePath = "/home/jared/Desktop/Sync/Loci"
workLogPath = basePath + "/work_logs"
journalPath = basePath + "/journal"

newLine = "\n"
twoNewLines = "\n\n"
smallDivider = "----------------"
mediumDivider = "------------------------------"
largeDivider = "---------------------------------------------"

def logWorkEntry():

    # Form the title for the work log
    date = datetime.datetime.now()
    # Weekday - Month - Day of Month - Year
    workLogEntryTitle = date.strftime("%a %b %d, %Y")

    # Start the outstring
    outString = ""
    outString = outString + "Work Log Entry" + newLine

    # Start the entry
    print("\n" + mediumDivider)
    print(workLogEntryTitle + " Work Log Entry")
    print(mediumDivider)

    # Record the date and time
    outString = outString + smallDivider + newLine
    outString = outString + date.strftime("%a %b %d, %Y - %I:%M %p")
    outString = outString + newLine + mediumDivider + newLine

    # Accomplishments
    accomplishments = input("\nWhat were some of your accomplishments today?\n\n")
    outString = outString + newLine + "Accomplishments" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + accomplishments) + twoNewLines

    # Difficulties
    difficulties = input("\nWhat were some of the difficulties you faced today?\n\n")
    outString = outString + newLine + "Difficulties" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + difficulties) + twoNewLines

    # Notes
    notes = input("\nEnter some notes about work today:\n\n")
    outString = outString + newLine + "Notes" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + notes) + twoNewLines

    # Productivity score
    productivity = input("\nWhat was your productivity level (from 1 to 10)?\n\n")
    outString = outString + newLine + "Productivity Score" + newLine + smallDivider + twoNewLines
    outString = outString + str("   " + productivity) + twoNewLines

    print("Outstring:\n")
    print(outString)

logWorkEntry()