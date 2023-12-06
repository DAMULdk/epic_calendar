import os
import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime as dt, timedelta
from typing import List, Dict
from time import sleep

#Should work
# To do:
# main.py > menu > time till
# fix and test this
# birthday if possible
# Comments
# Readme.md
# ALL


def find_file(name, path):
    """ Finds a file with given name. """
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def show_message(title, message):
    """ Displays window notification. """
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)


def load(file):
    """ Loads file content. """
    try:
        with open(file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        show_message("calendar.pyw error", "calendar.pyw can't find important files. Reinstall epic_calendar or check your system.")
        raise FileNotFoundError(f"File not found: {file}")
    except Exception as e:
        show_message("calendar.pyw error", f"calendar.pyw {e}. Reinstall epic_calendar or check your system.")
        raise FileNotFoundError(f"Error: {e}")
    

def save(data, file):
    """ Saves data to json file. """
    try:
        with open(file, 'w') as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError:
        found_file = full_load()[1] # Loads file path
        if found_file:
            save(data, found_file)
        else:
            return None

    except Exception as e:
        raise FileNotFoundError(f"Error: {e}")
    

def full_load():
    """ Finds the file and gets events from it. """
    found_paths = find_file("events.json", "/")
    found_file = ""
    for i in found_paths: # Looks for events.json in epic_calendar forlder
        if "epic_calendar" in i:
            found_file = i
    events: List[Dict] = load(found_file)
    return events, found_file


def main():
    name = "name"
    date = "date"
    desc = "description"
    repeat = "repetitive"
    time = "time"
    reminds = "reminders"

    while True:
        events, path = full_load() # Loading events
        print("Jeździ")

        for i in range(60):
            """ Checking whether an event occurred, 60 times to avoid loading 
            data each time, which could be incriminating for the system """
            now = dt.now()
            events = load(path) # Current events
            events_temp = [] # List that will contain edited events

            for event in events:
                event_temp = event

                date_time = event[date] + " " + event[time] # Converting event date and time to datetime object
                date_time = dt.strptime(date_time, "%Y-%m-%d %H:%M:%S")

                reminds_delta = timedelta(days=event[reminds]) # Coverting reminders to timedelta

                print(date_time)
                print(reminds_delta)
                print(event[reminds])
                print((date_time >= (now - reminds_delta)))
                print("\n\n\n\n")

                # Makes sure that event has not more reminders than days till this event
                while ((date_time - now).days < event[reminds] - 1) and event[reminds] > 0:
                    event_temp[reminds] -= 1

                # Checks if event happened
                if (date_time <= now) and event[reminds] >= 0:
                    message = f"""{event[name]}!
{event[desc]}
{event[date]} {event[time]}
                    """
                    event_temp[reminds] = -1
                    events_temp.append(event_temp)
                    show_message("Epic Calendar", message)

                # Checks if reminders should be displayed
                elif (now > (date_time - reminds_delta)) and event[reminds] >= 0:
                    event_temp[reminds] -= 1
                    events_temp.append(event_temp)
                    message = f"""{event[reminds] + 1} days till {event[name]}!
{event[desc]}
Event final date: {event[date]} {event[time]}
You have {event[reminds]} reminders left.
                    """
                    show_message("Epic Calendar", message)

                else:
                    events_temp.append(event_temp)

            save(events_temp, path) # Saves updated events to file
            sleep(2)


if __name__ == "__main__":
    main()