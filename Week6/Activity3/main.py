def main():
    # Dictionary 1
    student1 = {
        "name": "Alex",
        "age": 42,
        "course": "Data Analytics",
        "city": "Auckland",
        "status": "Lecturer"
    }
    
    # Dictionary 2
    student2 = {
        "name": "Sophia",
        "age": 29,
        "course": "Software Engineering",
        "city": "Wellington",
        "status": "Student"
    }
    
    # Dictionary 3
    student3 = {
        "name": "Michael",
        "age": 35,
        "course": "Cyber Security",
        "city": "Christchurch",
        "status": "Researcher"
    }

    students = [student1, student2, student3]
    # name with "zaw"
    merged_students1 = {
        **{
            key: value
            for student in students if "azw" in student["name"].lower()
            for key, value in student.items()
        }
    }

    print(merged_students1)

    # name value with "ex" pattern
    merged_students2 = {
        **{
            key: value
            for student in students if "ex" in student["name"].lower()
            for key, value in student.items()
        }
    }

    print(merged_students2)


if __name__ == "__main__":
    main()