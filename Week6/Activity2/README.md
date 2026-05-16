# Zoo Management System – Activity 2

A simple Python project that demonstrates **decorators** through an admin login system for a Zoo.

---

## Project Structure

```
Activity2/
├── decorators.py   # Two decorators: require_login and log_activity
├── zoo.py          # Admin login/logout and zoo animal management functions
├── main.py         # Entry point – runs the full demonstration
└── README.md       # This file
```

---

## Functionality

| Feature | Description |
|---|---|
| Admin Login | Validates username and password before granting access |
| Access Control | Blocked functions print "Access denied" if not logged in |
| View Animals | Displays all animals in a formatted table |
| Add Animal | Adds a new animal to the zoo list |
| Remove Animal | Removes an animal by name |
| Admin Logout | Clears login state and blocks further access |

**Admin credentials used in this project:**
- Username: `admin`
- Password: `zoo123`

---

## How the Decorators Work

### 1. `require_login` — Access Control Decorator

This decorator checks the shared `login_state` dictionary before running any zoo function.  
If the admin is **not logged in**, it prints an error and returns immediately (the real function never runs).  
If the admin **is logged in**, it proceeds normally.

```python
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not login_state["logged_in"]:
            print("Access denied. Please log in first.\n")
            return
        return func(*args, **kwargs)
    return wrapper
```

### 2. `log_activity` — Logging Decorator

This decorator wraps each function call with a formatted log block showing the function name, the logged-in admin's name, and the current timestamp.

```python
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
```

### Stacking Decorators

In `zoo.py`, both decorators are stacked on each admin function:

```python
@require_login
@log_activity
def view_animals():
    ...
```

Python applies decorators from **bottom to top**, so `log_activity` wraps the function first, then `require_login` wraps that. This means the login check happens **before** any logging output is printed.

---

## How to Run

```bash
python main.py
```

## Sample Output

```
========================================
       Zoo Management System            
========================================

--- Attempt to view animals WITHOUT login ---
Access denied. Please log in first.

--- Admin login with correct credentials ---
Welcome, admin! Login successful.

--- View all animals ---
===================================
Function : view_animals
Admin    : admin
Time     : 2026-05-16 21:48:07
Activity started...
No.   Name         Species         Age
------------------------------------------
1     Leo          Lion            5
2     Dumbo        Elephant        10
3     Nemo         Clownfish       2

Activity completed.
===================================
```
