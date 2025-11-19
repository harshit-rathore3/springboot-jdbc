import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

/**
 * A comprehensive StudentManager class
 * that handles:
 *  - CRUD operations
 *  - Searching
 *  - Sorting
 *  - Import/Export
 *  - File persistence
 *  - Statistics
 */
public class StudentManager {

    private List<Student> students = new ArrayList<>();

    // -------------------------------
    // BASIC CRUD METHODS
    // -------------------------------

    public boolean addStudent(Student student) {
        if (student == null || student.getId() <= 0) {
            return false;
        }
        if (getStudentById(student.getId()) != null) {
            return false; // duplicate ID
        }
        students.add(student);
        return true;
    }

    public boolean removeStudent(int id) {
        return students.removeIf(s -> s.getId() == id);
    }

    public Student getStudentById(int id) {
        return students.stream()
                .filter(s -> s.getId() == id)
                .findFirst()
                .orElse(null);
    }

    public boolean updateStudentName(int id, String newName) {
        Student s = getStudentById(id);
        if (s != null) {
            s.setName(newName);
            return true;
        }
        return false;
    }

    public boolean updateStudentGrade(int id, double grade) {
        Student s = getStudentById(id);
        if (s != null && grade >= 0 && grade <= 100) {
            s.setGrade(grade);
            return true;
        }
        return false;
    }

    public List<Student> getAllStudents() {
        return new ArrayList<>(students);
    }

    // -------------------------------
    // SEARCH FUNCTIONS
    // -------------------------------

    public List<Student> searchByName(String name) {
        return students.stream()
                .filter(s -> s.getName().toLowerCase().contains(name.toLowerCase()))
                .collect(Collectors.toList());
    }

    public List<Student> searchByMinimumGrade(double grade) {
        return students.stream()
                .filter(s -> s.getGrade() >= grade)
                .collect(Collectors.toList());
    }

    public List<Student> searchByGradeRange(double min, double max) {
        return students.stream()
                .filter(s -> s.getGrade() >= min && s.getGrade() <= max)
                .collect(Collectors.toList());
    }

    // -------------------------------
    // SORTING FUNCTIONS
    // -------------------------------

    public void sortByNameAscending() {
        students.sort(Comparator.comparing(Student::getName));
    }

    public void sortByNameDescending() {
        students.sort(Comparator.comparing(Student::getName).reversed());
    }

    public void sortByGradeAscending() {
        students.sort(Comparator.comparingDouble(Student::getGrade));
    }

    public void sortByGradeDescending() {
        students.sort(Comparator.comparingDouble(Student::getGrade).reversed());
    }

    public void sortById() {
        students.sort(Comparator.comparingInt(Student::getId));
    }

    // -------------------------------
    // STATISTICS
    // -------------------------------

    public double getAverageGrade() {
        return students.stream()
                .mapToDouble(Student::getGrade)
                .average()
                .orElse(0.0);
    }

    public Student getHighestGradeStudent() {
        return students.stream()
                .max(Comparator.comparingDouble(Student::getGrade))
                .orElse(null);
    }

    public Student getLowestGradeStudent() {
        return students.stream()
                .min(Comparator.comparingDouble(Student::getGrade))
                .orElse(null);
    }

    public int getTotalStudents() {
        return students.size();
    }

    // -------------------------------
    // FILE SAVE / LOAD (SERIALIZATION)
    // -------------------------------

    public boolean saveToFile(String fileName) {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(fileName))) {
            out.writeObject(students);
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    public boolean loadFromFile(String fileName) {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(fileName))) {
            students = (List<Student>) in.readObject();
            return true;
        } catch (IOException | ClassNotFoundException e) {
            return false;
        }
    }

    // -------------------------------
    // CSV IMPORT / EXPORT
    // -------------------------------

    public boolean exportCSV(String fileName) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fileName))) {
            pw.println("ID,Name,Grade");
            for (Student s : students) {
                pw.println(s.getId() + "," + s.getName() + "," + s.getGrade());
            }
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    public boolean importCSV(String fileName) {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            students.clear();
            String line;
            reader.readLine(); // skip header
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length != 3) continue;
                int id = Integer.parseInt(parts[0]);
                String name = parts[1];
                double grade = Double.parseDouble(parts[2]);
                students.add(new Student(id, name, grade));
            }
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    // -------------------------------
    // EXTRA UTILITY FUNCTIONS
    // -------------------------------

    public boolean studentExists(int id) {
        return getStudentById(id) != null;
    }

    public void clearAll() {
        students.clear();
    }

    public List<Student> getTopStudents(int count) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getGrade).reversed())
                .limit(count)
                .collect(Collectors.toList());
    }

    public List<Student> getBottomStudents(int count) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getGrade))
                .limit(count)
                .collect(Collectors.toList());
    }

    public List<Student> getStudentsAboveAverage() {
        double avg = getAverageGrade();
        return students.stream()
                .filter(s -> s.getGrade() > avg)
                .collect(Collectors.toList());
    }

    public List<Student> getStudentsBelowAverage() {
        double avg = getAverageGrade();
        return students.stream()
                .filter(s -> s.getGrade() < avg)
                .collect(Collectors.toList());
    }

    public void printAllStudents() {
        students.forEach(System.out::println);
    }
}
