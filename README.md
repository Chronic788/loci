# Loci

***Latin, meaning 'place'***

Loci is a little tool that helps you keep notes on your day.

I find one of the hardest things about being a professional software engineer is keeping track of the little things. At any point in time it is difficult to remember what happened just a short time ago. Loci is meant to be used daily to build a record of the little things that happened over time. If used consistently, it can build up a nice little record of what happened day to day.

It does so by asking 5 key questions:

1. What were some of your accomplishments today?
2. What were some of your difficulties today?
3. What are some specifics from today that you would like to remember?
4. What was your productivity level (from 1 to 10) and why?
5. What are you doing tomorrow?

I've boiled these particular questions as ones that are effective in giving a whole perspective of a day. Questions can easily be added and removed in the source code if you don't like one or have one that matters to you.

## What does loci do?

Loci is a script that runs from the command line. When you run it it will ask you the 5 questions above and then output a report to a file titled with the date and time that you can look at later.

## Set Up Loci

1. There are two important parameters in the source code to change to set up loci on your machine (both Windows and Linux are supported):

	1. The base path - The path where the work logs folder will reside. 
	
		On Windows, this defaults to 'C:\work_logs'
		On Linux, I have it set to my local machine so I recommend you change it to a directory of your choice.
	
	2. The log path name - What you want your work log folder to be named (leaving this as default is fine).
	
	  	These parameters reside at the top of the file and can be set for both Windows and Linux

2. Ensure that you have python installed on your machine

## Run Loci

1. Change directories to where the loci.py file is
2. Run this command: python loci.py

## What Happens?

Loci will take the answers to your questions and compile a little report in a text file at the location you specify. The file will be titled with the day and time for easy reference.

Try it out for a few days and see if it helps you keep track of your work!