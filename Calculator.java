public class Calculator {

    // Adds two numbers
    public double add(double a, double b) {
        return a + b;
    }

    // Subtracts second number from first
    public double subtract(double a, double b) {
        return a - b;
    }

    // Multiplies two numbers
    public double multiply(double a, double b) {
        return a * b;
    }

    // Divides first number by second (with zero check)
    public double divide(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Cannot divide by zero");
        }
        return a / b;
    }

    // Calculates remainder
    public double modulus(double a, double b) {
        return a % b;
    }

    // Main method to test the calculator
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        double x = 10;
        double y = 5;

        System.out.println("Addition: " + calc.add(x, y));
        System.out.println("Subtraction: " + calc.subtract(x, y));
        System.out.println("Multiplication: " + calc.multiply(x, y));
        System.out.println("Division: " + calc.divide(x, y));
        System.out.println("Modulus: " + calc.modulus(x, y));
    }
}
