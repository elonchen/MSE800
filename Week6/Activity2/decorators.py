# import system function
from datetime import datetime
from functools import wraps


# track login state across the application
login_state = {"logged_in": False, "username": ""}


# check if admin is logged in before allowing access
def require_login(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not login_state["logged_in"]:
            print("Access denied. Please log in first.\n")
            return
        return func(*args, **kwargs)

    return wrapper


# add same format & info, such as show function's name, current time of running, lines
def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("===================================")
        print(f"Function : {func.__name__}")
        print(f"Admin    : {login_state['username']}")
        print(f"Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
