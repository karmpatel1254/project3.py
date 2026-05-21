print("Welcome to Student Data Organizer!")

student = []

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Subjects")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        sid = input("Student ID: ")
        dob = input("Date of Birth: ")
        subjects = input("Subjects (comma separated): ")

        print("Student added")

    elif choice == "2":
        if not student:
            print("No students yet.")
        for s in student: 
            sid = s["id"]
            dob = s["dob"]
            print(f"sutdent added")

    elif choice == "3":
        sid = input("Enter Student ID to update: ")
        for s in student: 
            if s["id_dob"] == sid:
                s["age"] = input("New Age: ")
                s["subjects"] = set(input("New Subjects: ").split(","))
                print("Updated!")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        found = False
        for s in student: 
            if s["id"] == sid:
                s["dob"] == dob            
                student.remove(s)
                print("Deleted!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        subjects = set()
        for s in student: 
            subjects = s["subjects"]
        print("All Subjects:", ", ".join(subjects))

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")