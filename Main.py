"""
Jonathan Ishii
Andrew Ramirez
Joshua Logue
Hector Elias

Lab 2
"""

import sqlite3
import csv

def create_db():
    # reads in the CSV file and populates the database based off the CSV(s)
    create_competitor()
    create_event()
    create_awards()
    pass

def create_competitor(cur):
    # creates the competitors db

    # user_id (primary key), name, phone_number, sex, age, username, kills, deaths, wins, games_played
    cmd = """
    CREATE TABLE Competitors(
        user_id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        phone_number TEXT,
        sex VARCHAR(1) NOT NULL,
        age INTEGER NOT NULL,
        username TEXT NOT NULL,
        kills INTEGER,
        deaths INTEGER,
        wins INTEGER,
        games_played INTEGER
    );
    """
    cur.execute(cmd)

def create_event(cur):
    # creates the event db

    # event_id, time, event_name (solo, duo, squad, LTM limited time mode), user_id, team_id, win
    cmd = """
    CREATE TABLE EVENTS(
        event_id INTEGER PRIMARY KEY NOT NULL,
        time TEXT,
        event_name TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        team_id INTEGER,
        win INTEGER
    );
    """
    cur.execute(cmd)

def create_awards(cur):
    # creates the awards db

    # (solo_win, duo_win, squad_win) = umbrella , team_id
    cmd = """
    CREATE TABLE Awards(
        (solo_win, duo_win, squad_win) = umbrella , team_id

def create_account():
    """Function to create an account for a competitor."""
    pass

def edit_accout():
    """Function to edit an existing competitor's account"""
    pass

def delete_account():
    """Function to delete a competitor's account."""
    pass

def create_event():
    """Function to create an event."""
    pass

def enter_event():
    """Function to enroll a competitor into an event."""
    pass

def change_event():
    """Function to allow a competitor to change event."""
    pass

def remove_event():
    """Function to remove competitor from an event."""
    pass

def show_all_competitors():
    """Function to display all competitors."""
    pass

def show_male_competitors():
    """Function to display all male competitors."""
    pass

def show_female_competitors():
    """Function to display all female competitors."""
    pass

def show_all_events():
    """Function to display all events."""
    pass

def show_all_events_with_competitors():
    """Function to display all events with the competitors."""

def show_all_winners():
    """Function to display all the winners from all the events."""
    pass

def look_up_competitor():
    """Function to look up a competitor."""
    pass
def main():

    create_db()

    # allow the user to enter, modify, and delete records

    # contain at least one many-to-many relationship with a corresponding junction table

    # dynamically generate at least one graph of your database.
    # You might graph the number of awards each person earned, the times of the finishers, the average times, etc

    # you must be able to display (at least)
    # – All competitors alphabetically
    # – Competitors and their bib numbers (or whatever number they have) – All male competitors
    # – All female competitors
    # – All events, listed by starting time
    # – All of the competitors of each event
    # – The top winners of each event

    # You should allow the user to look up (at least)
    # – A person’s id given their name, event, and age
    # – A person’s information given their id number
    # – A person’s overall time (or whatever you’re tracking to determine winners) given their name or id (if matching by name, it’s OK if multiple people are returned)
    # – A person’s award(s) given their id number

    print("Welcome to FortniteCompetitionDB!")
    print("--------------------------------------------------------")
    print("This is a program for all users to create/edit accounts ")
    print("and events as well as displaying vital information.")
    print("--------------------------------------------------------")

    done = False
    while not done:
        print("\nPlease enter in a number from the options below.\n")
        print("1. Create account")
        print("2. Edit account.")
        print("3. Delete account.")
        print("4. Create an event.")
        print("5. Enter in an event.")
        print("6. Change event you are registered in.")
        print("7. Remove yourself from an event.")
        print("8. Show all competitors.")
        print("9. Show all male competitors.")
        print("10. Show all female competitors.")
        print("11. Show all events.")
        print("11. Show all events with competitors.")
        print("12. Show winners of all events.")
        print("13. Look up user.")
        print("\nEnter -1 to quit.")

        try:
            user_input = int(input("Choice: "))
        except ValueError:
            print("That is an invalid entry. Please try again.")
        else:
            if user_input < 0:
                done = True
            elif user_input is 1:
                pass
            elif user_input is 2:
                pass
            elif user_input is 3:
                pass
            elif user_input is 4:
                pass
            elif user_input is 5:
                pass
            elif user_input is 6:
                pass
            elif user_input is 7:
                pass
            elif user_input is 8:
                pass
            elif user_input is 9:
                pass
            elif user_input is 10:
                pass
            elif user_input is 11:
                pass
            elif user_input is 12:
                pass
            elif user_input is 13:
                pass
            else:
                print("Invalid Input: Please make a selection from one of the options .")



    print("\nThank you for using FortniteCompetitionDB.\nHave a nice day!")

if __name__ == "__main__":
    main()