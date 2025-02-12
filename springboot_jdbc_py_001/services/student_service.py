import logging
from models.student import Student
from repositories.student_repository import StudentRepository

class StudentService:
    def __init__(self, db_path: str):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.repository = StudentRepository(db_path)

    def run(self):
        # Find student by id
        student = self.repository.find_by_id(10001)
        self.logger.info(f"Student id 10001 -> {student}")

        # Insert a new student
        new_student = Student(id=10010, name="John", passport_number="A1234657")
        inserted = self.repository.insert(new_student)
        self.logger.info(f"Inserting -> {inserted}")

        # Update an existing student
        updated_student = Student(id=10001, name="Name-Updated", passport_number="New-Passport")
        updated = self.repository.update(updated_student)
        self.logger.info(f"Update 10001 -> {updated}")

        # Delete a student
        self.repository.delete_by_id(10002)

        # Find all students
        all_students = self.repository.find_all()
        self.logger.info(f"All users -> {all_students}")

def main():
    logging.basicConfig(level=logging.INFO)
    service = StudentService("path/to/your/database.db")
    service.run()

if __name__ == "__main__":
    main()