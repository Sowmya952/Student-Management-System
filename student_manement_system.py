class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, major):
        new_student = Student(student_id, name, age, major)
        self.students.append(new_student)
        print(f"Student {name} added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            print(student)

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student ID {student_id} deleted successfully.")
                return
        print(f"Student ID {student_id} not found.")

    def menu(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = input("Enter Student Age: ")
                major = input("Enter Student Major: ")
                self.add_student(student_id, name, age, major)
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                student_id = input("Enter Student ID to delete: ")
                self.delete_student(student_id)
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()
