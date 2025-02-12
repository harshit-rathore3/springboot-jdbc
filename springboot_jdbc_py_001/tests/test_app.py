import pytest
from app import main
from models.student import Student
from repositories.student_repository import StudentRepository
from services.student_service import StudentService
from unittest.mock import Mock

# Fixture for creating a test database and repository
@pytest.fixture
def student_repository():
    # Here we would typically set up a test database
    # For simplicity, we'll just return a new repository instance
    return StudentRepository()

@pytest.fixture
def student_service(student_repository):
    return StudentService(student_repository)

# Test finding a student by ID
def test_find_student_by_id(student_service):
    # Arrange
    test_student = Student(id=1, name="Test Student", passport_number="T12345")
    student_service.insert(test_student)
    
    # Act
    found_student = student_service.find_by_id(1)
    
    # Assert
    assert found_student is not None
    assert found_student.id == 1
    assert found_student.name == "Test Student"
    assert found_student.passport_number == "T12345"

# Test inserting a new student
def test_insert_student(student_service):
    # Arrange
    new_student = Student(id=2, name="New Student", passport_number="N67890")
    
    # Act
    inserted_student = student_service.insert(new_student)
    
    # Assert
    assert inserted_student is not None
    assert inserted_student.id == 2
    assert inserted_student.name == "New Student"
    assert inserted_student.passport_number == "N67890"

# Test updating an existing student
def test_update_student(student_service):
    # Arrange
    student = Student(id=3, name="Original Name", passport_number="O11111")
    student_service.insert(student)
    
    # Act
    student.name = "Updated Name"
    updated_student = student_service.update(student)
    
    # Assert
    assert updated_student is not None
    assert updated_student.id == 3
    assert updated_student.name == "Updated Name"
    assert updated_student.passport_number == "O11111"

# Test deleting a student
def test_delete_student(student_service):
    # Arrange
    student = Student(id=4, name="To Be Deleted", passport_number="D22222")
    student_service.insert(student)
    
    # Act
    deleted = student_service.delete(4)
    
    # Assert
    assert deleted is True
    assert student_service.find_by_id(4) is None

# Test retrieving all students
def test_find_all_students(student_service):
    # Arrange
    student1 = Student(id=5, name="Student One", passport_number="S11111")
    student2 = Student(id=6, name="Student Two", passport_number="S22222")
    student_service.insert(student1)
    student_service.insert(student2)
    
    # Act
    all_students = student_service.find_all()
    
    # Assert
    assert len(all_students) >= 2
    assert any(s.id == 5 and s.name == "Student One" for s in all_students)
    assert any(s.id == 6 and s.name == "Student Two" for s in all_students)

# Test main function (integration test)
def test_main_function(capsys):
    # Act
    main()
    
    # Assert
    captured = capsys.readouterr()
    assert "Student found" in captured.out
    assert "New student inserted" in captured.out
    assert "Student updated" in captured.out
    assert "Student deleted" in captured.out
    assert "All students" in captured.out

# Test finding a non-existent student
def test_find_non_existent_student(student_service):
    # Act
    non_existent_student = student_service.find_by_id(9999)
    
    # Assert
    assert non_existent_student is None

# Test student service with mocked repository
def test_student_service_with_mock():
    # Arrange
    mock_repo = Mock(spec=StudentRepository)
    mock_repo.find_by_id.return_value = Student(id=7, name="Mocked Student", passport_number="M33333")
    service = StudentService(mock_repo)
    
    # Act
    student = service.find_by_id(7)
    
    # Assert
    assert student is not None
    assert student.id == 7
    assert student.name == "Mocked Student"
    mock_repo.find_by_id.assert_called_once_with(7)

# Test database error handling
def test_database_error_handling(student_service, monkeypatch):
    # Arrange
    def mock_find_by_id(self, id):
        raise Exception("Database connection error")
    
    monkeypatch.setattr(StudentRepository, "find_by_id", mock_find_by_id)
    
    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        student_service.find_by_id(1)
    assert str(exc_info.value) == "Database connection error"