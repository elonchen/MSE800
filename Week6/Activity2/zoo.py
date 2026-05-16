# import decorators from another file
from decorators import require_login, log_activity, login_state


# admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "zoo123"

# initial zoo animal list
animals = [
    {"name": "Leo",   "species": "Lion",      "age": 5},
    {"name": "Dumbo", "species": "Elephant",  "age": 10},
    {"name": "Nemo",  "species": "Clownfish", "age": 2},
]


# login function - checks username and password
def admin_login(username, password):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        login_state["logged_in"] = True
        login_state["username"] = username
        print(f"Welcome, {username}! Login successful.\n")
    else:
        print("Invalid username or password. Please try again.\n")


# logout function - clears login state
def admin_logout():
    name = login_state["username"]
    login_state["logged_in"] = False
    login_state["username"] = ""
    print(f"Goodbye, {name}! You have been logged out.\n")


@require_login
@log_activity
def view_animals():
    print(f"{'No.':<5} {'Name':<12} {'Species':<15} {'Age'}")
    print("-" * 42)
    for i, animal in enumerate(animals, 1):
        print(f"{i:<5} {animal['name']:<12} {animal['species']:<15} {animal['age']}")
    print()


@require_login
@log_activity
def add_animal(name, species, age):
    animals.append({"name": name, "species": species, "age": age})
    print(f"New animal added: {name} ({species}), Age: {age}\n")


@require_login
@log_activity
def remove_animal(name):
    for animal in animals:
        if animal["name"].lower() == name.lower():
            animals.remove(animal)
            print(f"Animal removed: {name}\n")
            return
    print(f"Animal '{name}' not found in the zoo.\n")
