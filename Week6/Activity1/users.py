# import decorators from another file
from decorators import log_activity

@log_activity
# simulate login
def student_login(username):
    print(f"{username} logged into the system.")


@log_activity
# simulate submit
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")


@log_activity
# simulate view grade
def view_grades(username):
    print(f"{username} is viewing grades.")
