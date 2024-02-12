'''
This program uses the mysql connector to utilize python coding in order to add, edit,
or delete entries in the jobTracker database I created.
'''

import mysql.connector
import logging
import argparse

parser = argparse.ArgumentParser(description='Update entries for jobTracker database.')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('updateJobTracker.log', 'w')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

# set up mysql connection to jobTracker database
mydb = mysql.connector.connect(
    user = 'root',
    passwd = '***',
    database = 'jobTracker',
    host = '127.0.0.1',
    allow_local_infile = '1'
)

# set up the cursor
myc = mydb.cursor()

# make sure we are using the correct database
myc.execute("use jobTracker")
logging.info('Program Started')

# show existing tables
print("Existing tables in jobTracker: ")
myc.execute("show tables")
for x in myc:
    print('\t', x)

# Create a while loop that will return the user to the beginning once program completes.
# If user input is no, program will quit.
while True:

    # Ask user if they would like to make any changes to the existing tables
    userProgRunInput = str(input("Would you like to make changes to existing tables? ")).lower()

    # If yes, user will be asked which table they would like to make changes to.
    if userProgRunInput == "yes":
        logging.info('Change request acknowledged.')
        userInputQ = str(input("Good luck.")).lower()
        break

    # If no, user will be thanked and program will quit.
    elif userProgRunInput == "no":
        logging.info('Change request declined.')
        print("Thank you.")
        break

    # If invalid input used, user will be prompted again for input.
    else:
        logging.info('Invalid input recieved.')
        userProgRunInput = str(input("Not a valid option. Please answer yes/no. "))

mydb.commit()
mydb.close()
