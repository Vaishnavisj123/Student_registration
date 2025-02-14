# Initialize data structures
students = {}  # Dictionary to store student records
student_ids = []  # List to keep track of student IDs

# Main loop
while True:
    print("\n1. Add Student Record")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Information")
    print("5. Delete Student Record")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':  # Add Student Record
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        students[student_id] = {'name': name, 'age': age, 'grade': grade}
        student_ids.append(student_id)
        print("Student added successfully!")
        
    elif choice == '2':  # View All Students
        if not students:
            print("No students found.")
        else:
            for student_id in student_ids:
                student = students[student_id]
                print(f"ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                
    elif choice == '3':  # Search Student
        student_id = input("Enter student ID to search: ")
        if student_id in students:
            student = students[student_id]
            print(f"ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        else:
            print("Student not found.")
            
    elif choice == '4':  # Update Student Information
        student_id = input("Enter student ID to update: ")
        if student_id in students:
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            grade = input("Enter new grade: ")
            students[student_id] = {'name': name, 'age': age, 'grade': grade}
            print("Student information updated successfully!")
        else:
            print("Student not found.")
            
    elif choice == '5':  # Delete Student Record
        student_id = input("Enter student ID to delete: ")
        if student_id in students:
            del students[student_id]
            student_ids.remove(student_id)
            print("Student record deleted successfully!")
        else:
            print("Student not found.")
            
    elif choice == '6':  # Exit
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")
