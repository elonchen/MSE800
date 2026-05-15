# import functions from another file
from users import (
    student_login,
    submit_assignment,
    view_grades
)

# entrance function
def main():

    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")

# project start from here
if __name__ == "__main__":
    main()
