# import functions from another file
from zoo import (
    admin_login,
    admin_logout,
    view_animals,
    add_animal,
    remove_animal,
)


# entrance function
def main():
    print("========================================")
    print("       Zoo Management System            ")
    print("========================================\n")

    # attempt to access without login (should be denied)
    print("--- Attempt to view animals WITHOUT login ---")
    view_animals()

    # admin login with wrong password
    print("--- Admin login with wrong password ---")
    admin_login("admin", "wrongpass")

    # admin login with correct credentials
    print("--- Admin login with correct credentials ---")
    admin_login("admin", "zoo123")

    # view current animal list
    print("--- View all animals ---")
    view_animals()

    # add a new animal
    print("--- Add a new animal ---")
    add_animal("Simba", "Tiger", 3)

    # view updated list
    print("--- View updated animal list ---")
    view_animals()

    # remove an animal
    print("--- Remove an animal ---")
    remove_animal("Nemo")

    # view final list
    print("--- View final animal list ---")
    view_animals()

    # admin logout
    print("--- Admin logout ---")
    admin_logout()

    # attempt to access after logout (should be denied)
    print("--- Attempt to view animals AFTER logout ---")
    view_animals()


# project starts from here
if __name__ == "__main__":
    main()
