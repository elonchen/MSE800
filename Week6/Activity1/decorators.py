# import system function
from datetime import datetime


# add same format & info, such as show function's name, current time of running, lines
def log_activity(func):

    def wrapper(*args, **kwargs):
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
