"""
This file contains main application logic.
"""

import json
from colorama import Fore, just_fix_windows_console, init
from datetime import datetime as dt
from typing import Literal, Union, Any
from datetime import datetime as dt, time, date, timedelta

# Initialization
just_fix_windows_console()
init(autoreset=True)

class Calendar:
    def __init__(self):
        self.events = []
        self.load_events()

    def add_event(self, name, date, description, *args, **kwargs):
        """ Adds an event to the calendar. """
        new_event = Event(name, date, description, *args, **kwargs)
        self.events.append(new_event)
        self.save_events()
        return new_event

    def view_events(self):
        """ Prints all events in the calendar. """
        if not self.events:
            return f"{Fore.YELLOW}[i] No saved events in calendar"
        else:
            event_list = []
            for i, event in enumerate(self.events, start=1):
                if event.time != "00:00:00":
                    event_list.append(f"{i}. {event.name} - {event.date} {event.time}: {event.description}")
                elif event.reminders != 1:
                    event_list.append(f"{i}. {event.name} - {event.date}. reminders left: {event.reminders}: {event.description}")
                else:
                    event_list.append(f"{i}. {event.name} - {event.date}: {event.description}")
            return "\n".join(event_list)

    def delete_event(self, index):
        """ Deletes an event by index. """
        if index < 1 or index > len(self.events):
            return f"{Fore.RED}[!] Wrong index number"
        else:
            deleted_event = self.events.pop(index - 1)
            self.save_events()
            return deleted_event

    def clear_events(self):
        """ Clear all events from the calendar. """
        self.events = []
        self.save_events()

    def till_event(self, index):
        """ Shows time till index with given index. """
        if not 1 <= index <= len(self.events):
            return f"{Fore.RED}[!] Wrong index number"

        event_date = dt.strptime(self.events[index - 1].date + " " + self.events[index -1].time, "%Y-%m-%d %H:%M:%S")
        now = dt.now()

        print(event_date)
        print(now)
        print(event_date - now)

        if event_date < now:
            if self.events[index - 1].repetitive:
                event_date = event_date.replace(year=event_date.year + 1)
            else:
                delta = (event_date - now)
                return delta

        delta = (event_date - now)
        return delta


    def default(self):
        """ Sets default events. """
        try:
            default_events = [
                {"name": "Independence Day in Poland",
                 "date": "2222-11-11",
                 "description": "Celebrating Poland's Independence Day",
                 "repetitive": True,
                 "time": "00:00:00",
                 "reminders": 1},
                {"name": "Independence Day in USA",
                 "date": "2023-7-04",
                 "description": "Celebrating American Independence",
                 "repetitive": True,
                 "time": "00:00:00",
                 "reminders": 1},
                {"name": "Easter",
                 "date": "2222-04-07",
                 "description": "Celebration of the resurrection of Jesus",
                 "repetitive": True,
                 "time": "00:00:00",
                 "reminders": 1},
                {"name": "Christmas",
                 "date": "2222-12-25",
                 "description": "Celebrating the birth of Jesus Christ",
                 "repetitive": True,
                 "time": "00:00:00",
                 "reminders": 1}
            ]

            with open("events.json", "w+") as f:
                json.dump(default_events, f, indent=4)
            print(f"{Fore.YELLOW}[i] Created events.json with default events")
            self.load_events()
            return self.events
        except Exception as e:
            return e

    def load_events(self):
        """ Loads events from file events.json. """
        try:
            with open("events.json", "r") as f:
                events_data = json.load(f)
                self.events = [Event(**event) for event in events_data]

        except FileNotFoundError:
            self.default()
            print(f"{Fore.RED}[!] File events.json not found")

        except ValueError:
            self.default()
            print(f"{Fore.RED}[!] Ups, something went wrong. Restarting the program recommended")

        except Exception as e:
            self.default()
            print(f"{Fore.RED}[!] {e}")

    def save_events(self):
        """ Saves events to file events.json. """
        try:
            with open("events.json", "w") as f:
                events_data = [vars(event) for event in self.events]
                json.dump(events_data, f, indent=4)
        except FileNotFoundError:
            return f"{Fore.RED}[!] File events.json not found"

        except Exception as e:
            return e

class Event:
    """ Event object. """
    def __init__(self, name, date, description, repetitive=False, time="00:00:00", reminders=1):
        self.name = name
        self.date = date
        self.description = description
        self.repetitive = repetitive
        self.time = time
        self.reminders = reminders

def save(user_info):
    """ Saves user's options and info into options.txt. """
    try:
        dark_mode, name, surname, birthday = user_info
        with open("options.txt", "w") as f:
            f.write(f"{dark_mode}\n{name}\n{surname}\n{birthday}\n")
        return f"{Fore.YELLOW}[i] Options updated"

    except FileNotFoundError:
        return f"{Fore.RED}[!] File options.txt not found. Restarting the program recommended"

    except PermissionError:
        return f"{Fore.RED}[!] [!] No file permissions"

    except Exception as e:
        return f"{Fore.RED}[!] {e}"


def load():
    """ Loads user's options and info from options.txt or creates options.txt if it doesn't exist. """
    def set_default_values(): # Nested function that sets default values
        """ Sets default values and saves them into options.txt. """
        dark_mode = True
        name = "User"
        surname = "User"
        birthday = "2000-01-01"
        user_info = (dark_mode, name, surname, birthday)
        save(user_info)
        print(f"{Fore.YELLOW}[i] Created options.txt with default options")
        return user_info

    try:
        with open("options.txt", "r") as f:
            options = [line.strip() for line in f]

        if options and len(options) == 4: # Checks if options.txt is valid, if not, sets default values
            global dark_mode, name, surname, birthday
            dark_mode = options[0].lower() == "true"
            name, surname, birthday = options[1:4]
            user_info = (dark_mode, name, surname, birthday)
            return user_info
        
        else:
            return set_default_values()

    except FileNotFoundError:
        print(f"{Fore.RED}[!] File options.txt not found")
        return set_default_values()

    except PermissionError:
        print(f"{Fore.RED}[!] No file permissions")
        return set_default_values()

    except Exception as e:
        print(f"{Fore.RED}[!] {e}")
        return set_default_values()


def is_valid(
    value: str,
    data_type: Literal["text", "int", "float", "date", "time", "confirm", "any"],
    min_val: Union[float, str, int] = float("-inf"),
    max_val: Union[float, str, int] = float("inf"),
    return_err_code: bool = False,
    date_format:str = "%Y-%m-%d",
    time_format:str = "%H:%M:%S"
) -> bool | int:
    """
    Checks if the given value matches the specified type and range.
    
    Args:
        value (str): The value to be validated.
        data_type (Literal["text", "int", "float", "date", "time", "confirm", "any"]): Expected data type for validation.
        min_val (Union[float, str, int]): Minimum constraint for the input value. Defaults to float("-inf").
        max_val (Union[float, str, int]): Maximum constraint for the input value. Defaults to float("inf").
        return_err_code (bool): If True, return error codes instead of boolean result. Defaults to False.
        date_format (str): Sets valid format for date. Defaults to "%Y-%m-%d".
        time_format (str): Sets valid format for time. Defaults to "%H:%M:%S".
        
    Returns:
        bool | int: If return_err_code is True, returns an integer representing an error code. If False, returns a boolean indicating whether the value is valid.
        
    Error Codes:
        0: No error / valid
        1: Value is empty
        2: Wrong value type
        3: Too low value
        4: Too high value

    Note:
        For "date" data_type, min_val and max_val should be date represented by date in string in format set by date_format.
        For "time" data_type, min_val and max_val should be date represented by time in string in format set by time_format.
        For "text" data_type, min_val and max_val is int that represents minimal and maximal length of value to be validated.
        For "int" and "float", min_val and max_val should be int or float.
    """
    # Check for empty input
    if not value:
        return (False if not return_err_code else 1)
    
    # Validate based on data type

    # Checks for text, min_val and max_val represends minimum and maximum value lenght
    if data_type == 'text':
        if len(value) < min_val or len(value) > max_val:
            return (False if not return_err_code else (3 if len(value) < min_val else 4))
        else:
            return (True if not return_err_code else 0)
    # Checks for int
    elif data_type == 'int':
        try:
            num = int(value)
            if num < min_val or num > max_val:
                return (False if not return_err_code else (3 if num < min_val else 4))
            else:
                return (True if not return_err_code else 0)
        except ValueError:
            return (False if not return_err_code else 2)
    # Checks for float
    elif data_type == 'float':
        try:
            num = float(value)
            if num < min_val or num > max_val:
                return (False if not return_err_code else (3 if num < min_val else 4))
            else:
                return (True if not return_err_code else 0)
        except ValueError:
            return (False if not return_err_code else 2)
    # Checks for date, value "date_format" is valid format for date, default is "%Y-%m-%d"
    # min_val and max_val represents minimal and maximal date and they should be strings in set date_format
    elif data_type == 'date':
        try:
            date = dt.strptime(value, date_format).date()
            min_date = dt.strptime(min_val, date_format).date() if isinstance(min_val, str) else dt.min.date()
            max_date = dt.strptime(max_val, date_format).date() if isinstance(max_val, str) else dt.max.date()
            if date < min_date or date > max_date:
                return (False if not return_err_code else (3 if date < min_date else 4))
            else:
                return (True if not return_err_code else 0)
        except:
            return (False if not return_err_code else 2)
    # Checks for time, value "time_format" is valid format for time, default is "%H:%M:%S"
    # min_val and max_val represents minimal and maximal time and they should be strings in set time_format
    elif data_type == 'time':
        try:
            time = dt.strptime(value, time_format).time()
            min_time = dt.strptime(min_val, time_format).time() if isinstance(min_val, str) else dt.min.time()
            max_time = dt.strptime(max_val, time_format).time() if isinstance(max_val, str) else dt.max.time()
            if time < min_time or time > max_time:
                return (False if not return_err_code else (3 if time < min_time else 4))
            else:
                return (True if not return_err_code else 0)
        except:
            return (False if not return_err_code else 2)
    elif data_type == 'confirm':
        if value.lower() in ('y', 'yes', '1', 'n', 'no', '0'):
            return (True if not return_err_code else 0)
        else:
            return (False if not return_err_code else 2)
    # Check for any data type by converting to common types (date, time, int, float)
    elif data_type == 'any':
        vals = []
        for val in [value, str(min_val), str(max_val)]:
            if is_valid(val, "date"):
                vals.append(dt.strptime(val, date_format))
            elif is_valid(val, "time"):
                vals.append(dt.strptime(val, time_format))
            elif is_valid(val, "int") or is_valid(val, "float"):
                vals.append(float(val))
            else:
                if val == value:
                    vals.append(len(val))
        
        vals = tuple(vals)    
        value, min_val, max_val = vals

        try:
            if value < min_val or value > max_val:
                return (False if not return_err_code else (3 if value < min_val else 4))
            else:
                return (True if not return_err_code else 0)
        except:
            return (False if not return_err_code else 2)

def validator(
    text: str,
    data_type: Literal["text", "int", "float", "date", "time", "confirm"],
    repeat: bool = True,
    min_val: Union[float, str, int] = float("-inf"),
    max_val: Union[float, str, int] = float("inf"),
    nothing_err: str = f"{Fore.RED}[!] Nothing has been entered",
    type_err: str = f"{Fore.RED}[!] Wrong input type",
    low_err: str = f"{Fore.RED}[!] Input value is too low",
    high_err: str = f"{Fore.RED}[!] Input value is too high",
    date_format: str = "%Y-%m-%d",
    time_format: str = "%H:%M:%S"
) -> Any:
    """
    Validate user input.

    Args:
        text (str): Prompt text for the user input.
        data_type (Literal["text", "int", "float", "date", "time", "confirm"]): Expected data type for input.
        repeat (bool): If True, allow the user to retry input on error. Defaults to True.
        min_val (Union[float, str, int]): Minimum constraint for the input value. Defaults to float("-inf").
        max_val (Union[float, str, int]): Maximum constraint for the input value. Defaults to float("inf").
        nothing_err (str): Error message for empty input. Defaults to "Nothing has been entered".
        type_err (str): Error message for incorrect input type. Defaults to "Wrong input type".
        low_err (str): Error message for input value below the minimum constraint. Defaults to "Input value is too low".
        high_err (str): Error message for input value above the maximum constraint. Defaults to "Input value is too high".
        date_format (str): Sets valid format for date. Defaults to "%Y-%m-%d".
        time_format (str): Sets valid format for time. Defaults to "%H:%M:%S".

    Returns:
        Any: Validated and processed user input based on the specified data type.

    Note:
        min_val and max_val works the same as in is_valid(...) function.
    """
    while True:
        # Gets user input
        user_input = input(text)

        # Checks for empty input
        if not user_input:
            print(nothing_err)
            if not repeat:
                return None
            else:
                continue

        # Validates input
        output = is_valid(user_input, data_type, min_val, max_val, True, date_format, time_format)

        # Handles different error codes
        if output == 1:
            print(nothing_err)
        elif output == 2:
            print(type_err)
        elif output == 3:
            print(low_err)
        elif output == 4:
            print(high_err)
        else:
            # Process and returns validated input based on data type
            if data_type == "text":
                return str(user_input).strip()
            elif data_type == "int":
                return int(user_input)
            elif data_type == "float":
                return float(user_input)
            elif data_type == "date":
                return dt.strptime(user_input, date_format).date()
            elif data_type == "time":
                return dt.strptime(user_input, time_format).time()
            elif data_type == "confirm":
                return True if user_input.lower() in ('y', 'yes', '1') else False
            else:
                return None  # Handles unknown data types

        # If repeat is False, exits the loop
        if not repeat:
            return None
        


def adv_dt_validator(
    text: str,
    data_type: Literal["datetime", "date", "time"],
    repeat: bool = True,
    nothing_err: str = f"{Fore.RED}[!] Nothing has been entered",
    type_err: str = "",
    past_err: str = "",
    date_format: str = "%Y-%m-%d",
    time_format: str = "%H:%M:%S",
    conv_to_str: bool = True
) -> Union[date, time, dt] | str | tuple:
    """
    Validates and processes user input for date, time, or date and time for them to be in the future.

    Parameters:
    - text (str): The prompt text for user input.
    - data_type (Literal["datetime", "date", "time"]): Type of data to validate.
    - repeat (bool): If True, allows the user to repeat the input in case of an error.
    - nothing_err (str): Custom error message for when nothing is entered.
    - type_err (str): Custom error message for invalid input format.
    - past_err (str): Custom error message for input in the past.
    - date_format (str): Format for date (default: "%Y-%m-%d").
    - time_format (str): Format for time (default: "%H:%M:%S").
    - conv_to_str (bool): If True, converts the result to a string (default: True).

    Returns:
    - Union[date, time, dt] | str | tuple: Processed and validated result.

    Example Usage:
    - To get a valid date: adv_dt_validator("Enter date: ", "date")
    - To get a valid time: adv_dt_validator("Enter time: ", "time")
    - To get a valid datetime: adv_dt_validator("Enter datetime: ", "datetime")

    Note:
    - Function made specific for "Epic calendar" app.
    """

    # Checks if date entered by user isn't in the past
    if data_type == "date":
        v_date = validator(text, "date", repeat, 
            min_val=dt.strftime(dt.today() + timedelta(days=1), "%Y-%m-%d"), 
            nothing_err=nothing_err,
            type_err=type_err if type_err else 
            f"{Fore.RED}Invalid date format\nExample of correct date: {dt.strftime(dt.today() + timedelta(days=5), date_format)}",
            low_err=past_err if past_err else f"{Fore.RED}[!] date you entered has already passed"
        )
        return dt.strftime(v_date, date_format) if conv_to_str else v_date
    
    # Checks if time entered by user isn't in the past
    elif data_type == "time":
        v_time = validator(text, "time", repeat, 
            min_val=dt.strftime(dt.today() + timedelta(days=1), "%H:%M:%S"), 
            nothing_err=nothing_err,
            type_err=type_err if type_err else
            f"{Fore.RED}Invalid time format\nExample of correct time: {dt.strftime(dt.today() + timedelta(hours=1), time_format)}",
            low_err=past_err if past_err else f"{Fore.RED}[!] time you entered has already passed"
        )
        return time.strftime(v_time, time_format) if conv_to_str else v_time
    
    # Checks if date and time entered by user isn't in the past
    elif data_type == "datetime":
        v_date = validator(text, "date", repeat,
            min_val=dt.strftime(dt.today(), "%Y-%m-%d"),
            nothing_err=nothing_err,
            type_err=type_err if type_err else
            f"{Fore.RED}Invalid date format\nExample of correct date: {dt.strftime(dt.today() + timedelta(days=5), date_format)}",
            low_err=past_err if past_err else f"{Fore.RED}[!] date you entered has already passed"
        )

        if v_date == date.today(): # If the date is set to today, the time must be greater than the current time
            v_time = validator(text.replace("date", "time"), "time", repeat, 
                min_val=dt.strftime(dt.today(), "%H:%M:%S"),
                nothing_err=nothing_err,
                type_err=f"{Fore.RED}Invalid time format\nExample of correct time: {dt.strftime(dt.today() + timedelta(hours=1), time_format)}",
                low_err=past_err if past_err else f"{Fore.RED}[!] time you entered has already passed"
            )
        else: # If the date in't set to today, the time can be any
            v_time = validator(text.replace("date", "time"), "time", repeat, 
                nothing_err=nothing_err,
                type_err=f"{Fore.RED}Invalid time format\nExample of correct time: {dt.strftime(dt.today() + timedelta(hours=1), time_format)}"
            )
        
        event_datetime = dt.strptime(f"{v_date} {v_time}", "%Y-%m-%d %H:%M:%S")
        return (date.strftime(v_date, date_format), time.strftime(v_time, time_format)) if conv_to_str else event_datetime
    

def cal_prompt(data_type: Literal["normal", "+time", "+reminds"]):
    """ Function made for epic calendar app. Validates user's input for creating new events. """
    # Prompts for normal events adding
    if data_type == "normal":
        e_name = validator("Enter event name: ", "text", True, max_val=20)
        e_date = adv_dt_validator("Enter event date: ", "date")
        e_desc = validator("Event description: ", "text")
        return e_name, e_date, e_desc
    # Prompts for events with time (alarms) adding
    elif data_type == "+time":
        e_name = validator("Enter event name: ", "text", True, max_val=20)
        e_date, e_time = adv_dt_validator("Enter event date: ", "datetime")
        e_desc = validator("Event description: ", "text")
        return e_name, e_date, e_time, e_desc
    # Prompts for events with reminders (important events) adding
    elif data_type == "+reminds":
        e_name = validator("Enter event name: ", "text", True, max_val=20)
        e_date = adv_dt_validator("Enter event date: ", "date")
        e_desc = validator("Event description: ", "text")
        e_reminds = validator("How many reminders: ", "int", 
            min_val=1, max_val=(dt.strptime(e_date, "%Y-%m-%d").date() - dt.today().date()).days,
            low_err=f"{Fore.YELLOW}[i] You must have at least 1 reminder",
            high_err=f"{Fore.YELLOW}[i] You cannot have more reminders than the number of days until the event"
        )
        return e_name, e_date, e_desc, e_reminds