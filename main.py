"""
Zadanie zaliczeniowe z języka Python
Imię i nazwisko ucznia: Damian Kwasigroch
Data wykonania zadania: 06.12.2023
Treść zadania: Kalendarz z funkcją powiadomień
Opis funkcjonalności aplikacji: - w README.md
"""
"""
This file contains console ui for calendar management.
"""

import system as cal
import os
from time import sleep
from datetime import datetime as dt

from ctypes import windll
from colorama import Fore, just_fix_windows_console, init
from threading import Thread
import subprocess


windll.kernel32.SetConsoleTitleW("Epic Calendar " + dt.now().strftime("%Y-%m-%d %H:%M:%S"))
just_fix_windows_console()
init(autoreset=True)


def intro(user_info):
    """ Prints introduction. """
    dark_mode, name, surname, birthday = user_info
    art = """
███████╗██████╗ ██╗ ██████╗     ██████╗ █████╗ ██╗     ███████╗███╗   ██╗██████╗  █████╗ ██████╗ 
██╔════╝██╔══██╗██║██╔════╝    ██╔════╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗
█████╗  ██████╔╝██║██║         ██║     ███████║██║     █████╗  ██╔██╗ ██║██║  ██║███████║██████╔╝
██╔══╝  ██╔═══╝ ██║██║         ██║     ██╔══██║██║     ██╔══╝  ██║╚██╗██║██║  ██║██╔══██║██╔══██╗
███████╗██║     ██║╚██████╗    ╚██████╗██║  ██║███████╗███████╗██║ ╚████║██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
"""
    intro_info = (
    "By: Damian Kwasigroch\n" + 
    "Version: 0.1\n" + 
    "Created: 21.11.2023\n" + 
    "Last modified: 06-12-2023\n\n" +
    "Hello " + name + "\n" )
    print(Fore.LIGHTBLUE_EX + art + Fore.BLUE + intro_info)


def menu(user_info):
    """ Prints menu options. """
    dark_mode, name, surname, birthday = user_info
    print(Fore.LIGHTBLACK_EX + f"""
=======================================================
0 - See your events
1 - Add new event
2 - Add important event (with reminders)
3 - Add alarm (with time)
4 - Delete event (by index)
5 - Clear all events
6 - See time until event (by index)
7 - Clear console
8 - Change to {'bright' if dark_mode else 'dark'} mode (visible in gui)
9 - Add/Change user's info
10 - Go to gui version
11 - Exit
=======================================================          
""")
    

def options(calendar: cal.Calendar, user_info: tuple): # Big tree of user options
    dark_mode, name, surname, birthday = user_info
    while True:
        answer = cal.validator("Option: ", "int", True, min_val=0, max_val=11)
        if answer == 0: # See events
            print(calendar.view_events())

        elif answer == 1: # Add event
            e_name, e_date, e_desc = cal.cal_prompt("normal")
            added_event = calendar.add_event(e_name, e_date, e_desc)
            print(f"{Fore.GREEN}[+] Added {added_event.name} at {added_event.date}")
            calendar.save_events()

        elif answer == 2: # Add important event
            e_name, e_date, e_desc, e_reminds = cal.cal_prompt("+reminds")
            added_event = calendar.add_event(e_name, e_date, e_desc, reminders=e_reminds)
            print(f"{Fore.GREEN}[+] Added {added_event.name} at {added_event.date} with {added_event.reminders} reminders")
            calendar.save_events()

        elif answer == 3: # Add alarm
            e_name, e_date, e_time, e_desc = cal.cal_prompt("+time")
            added_event = calendar.add_event(e_name, e_date, e_desc, time=e_time)
            print(f"{Fore.GREEN}[+] Added {added_event.name} at {added_event.date} {added_event.time}")
            calendar.save_events()

        elif answer == 4: # Delete event
            index = cal.validator("Event index to delete: ", "int")
            print(calendar.delete_event(index))
            calendar.save_events()

        elif answer == 5: # delete all events
            confirm = cal.validator(f"{Fore.GREEN}Are you sure? [y/n]: {Fore.WHITE}", 
                "confirm", False, 
                type_err=f"{Fore.RED}[i] Expected y or n (yes or no)"
            )
            if confirm:
                calendar.clear_events()
                print(f"{Fore.GREEN}[-] Events cleared")
            calendar.save_events()

        elif answer == 6: # See time until event
            index = cal.validator("Event index to show: ", "int")
            time_till = calendar.till_event(index)
            day_time = 86400 * time_till.days
            print(f"""time till {
calendar.events[index-1].name}:
    in days: {time_till.days} days
    in hours: {(day_time + time_till.seconds) / 3600} hours
    in minutes: {(day_time + time_till.seconds) / 60} minutes
    in seconds: {day_time + time_till.seconds} seconds
    in universal python timedelta notation: {time_till}
            """)

        elif answer == 7: # Clear console
            clear_console()

        elif answer == 8:
            dark_mode = not user_info[0]
            user_info = (dark_mode, user_info[1], user_info[2], user_info[3])
            print(Fore.GREEN + f"[+] Changed to {'dark' if dark_mode else 'bright'} mode")
            cal.save(user_info)

        elif answer == 9: # Change user info
            name = cal.validator("Enter name: ", "text", max_val=20)
            surname = cal.validator("Enter surname: ", "text", max_val=20)
            birthday = cal.validator("Enter your birthday: ", "date")
            user_info2 = (user_info[0], name, surname, birthday)
            cal.save(user_info2)

        elif answer == 10: # Run main.pyw
            subprocess.run("python main.pyw")
            calendar.load_events()

        elif answer == 11: # Exit
            exit_calendar()


def clear_console():
    """ Clears console. """
    os.system('cls')
    menu(cal.load())

def title():
    """ Creates a loop that displays the updated date and time in the title bar every second. """
    while stay_cal:
        sleep(1)
        windll.kernel32.SetConsoleTitleW("Epic Calendar " + dt.now().strftime("%Y-%m-%d %H:%M:%S"))

def exit_calendar():
    """ Exits the program. """
    print(Fore.YELLOW + "[!] Exiting...")
    sleep(1)
    global stay_cal
    stay_cal = False # stay_cal is a variable that tells whether the program is running
    exit()


def main():
    # Creates important variables
    global stay_cal
    stay_cal = True
    calendar = cal.Calendar()

    dark_mode, name, surname, birthday = cal.load()
    user_info = (dark_mode, name, surname, birthday)

    # Shows console menu
    intro(user_info)
    menu(user_info)

    # Makes 2 threads, first for displaying and operating options and second for refreshing title with current date and time
    thread1 = Thread(args=[calendar, user_info], target=options)
    thread2 = Thread(target=title)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()