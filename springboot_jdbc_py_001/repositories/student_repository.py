import sqlite3
from typing import List, Optional
from models.student import Student

class StudentRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _student_row_mapper(self, row) -> Student:
        return Student(id=row[0], name=row[1], passport_number=row[2])

    def find_all(self) -> List[Student]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")
            return [self._student_row_mapper(row) for row in cursor.fetchall()]

    def find_by_id(self, id: int) -> Optional[Student]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student WHERE id=?", (id,))
            row = cursor.fetchone()
            return self._student_row_mapper(row) if row else None

    def delete_by_id(self, id: int) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student WHERE id=?", (id,))
            conn.commit()

    def insert(self, student: Student) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO student (id, name, passport_number) VALUES (?, ?, ?)",
                (student.id, student.name, student.passport_number)
            )
            conn.commit()
            return cursor.rowcount

    def update(self, student: Student) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE student SET name = ?, passport_number = ? WHERE id = ?",
                (student.name, student.passport_number, student.id)
            )
            conn.commit()
            return cursor.rowcount