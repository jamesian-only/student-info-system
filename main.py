import os
import logging
from src.services.student_service import StudentService

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

class StudentInformationSystem:
    def __init__(self):
        self.student_service = StudentService()
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
        print("\n=== Student Information System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def add_student(self):
        print("\n=== Add New Student ===")
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        year_level = input("Year Level: ")
        gpa = input("GPA: ")

        student_data = {
            'name': name,
            'email': email,
            'course': course,
            'year_level': year_level,
            'gpa': gpa
        }

        try:
            student = self.student_service.add_student(student_data)
            self.logger.info(f"Added student: {student['student_id']}")
            print(f"Student added successfully! ID: {student['student_id']}")
        except Exception as e:
            self.logger.error(f"Error adding student: {e}")
            print("Error adding student.")

    def view_all_students(self):
        print("\n--- All Students ---")
        students = self.student_service.get_all_students()
        if not students:
            print("No students found.")
            return
        for s in students:
            print(f"ID: {s['student_id']} | Name: {s['name']} | Email: {s['email']} | Course: {s['course']} | Year: {s['year_level']}")

    def view_student_by_id(self):
        student_id = input("Enter Student ID: ")
        student = self.student_service.get_student(student_id)
        if student:
            print(f"\nStudent Details: {student}")
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        print("Leave a field blank to keep current value.")
        name = input("New Name: ")
        email = input("New Email: ")
        course = input("New Course: ")
        year_level = input("New Year Level: ")
        gpa = input("New GPA: ")

        update_data = {k: v for k, v in {
            'name': name,
            'email': email,
            'course': course,
            'year_level': year_level,
            'gpa': gpa
        }.items() if v}

        updated = self.student_service.update_student(student_id, update_data)
        if updated:
            print("Student updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        deleted = self.student_service.delete_student(student_id)
        if deleted:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.view_student_by_id()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()
