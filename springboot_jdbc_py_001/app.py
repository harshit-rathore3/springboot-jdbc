import logging
from models.student import Student
from repositories.student_repository import StudentRepository

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Initialize the StudentRepository with the database path
    repository = StudentRepository('student.db')

    # Find student by ID
    student = repository.find_by_id(10001)
    logger.info(f"Student id 10001 -> {student}")

    # Insert a new student
    new_student = Student(id=10010, name="John", passport_number="A1234657")
    inserted = repository.insert(new_student)
    logger.info(f"Inserting -> {inserted}")

    # Update an existing student
    updated_student = Student(id=10001, name="Name-Updated", passport_number="New-Passport")
    updated = repository.update(updated_student)
    logger.info(f"Update 10001 -> {updated}")

    # Delete a student
    repository.delete_by_id(10002)

    # Find all students
    all_students = repository.find_all()
    logger.info(f"All users -> {all_students}")

if __name__ == "__main__":
    main()