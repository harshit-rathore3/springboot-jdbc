public class TemperatureConverter {

    // Convert Celsius to Fahrenheit
    public double celsiusToFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    // Convert Fahrenheit to Celsius
    public double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    // Convert Celsius to Kelvin
    public double celsiusToKelvin(double celsius) {
        return celsius + 273.15;
    }

    // Convert Kelvin to Celsius
    public double kelvinToCelsius(double kelvin) {
        return kelvin - 273.15;
    }

    // Main method to test the converter
    public static void main(String[] args) {
        TemperatureConverter converter = new TemperatureConverter();

        double c = 25.0;
        double f = 77.0;
        double k = 300.0;

        System.out.println(c + "°C = " + converter.celsiusToFahrenheit(c) + "°F");
        System.out.println(f + "°F = " + converter.fahrenheitToCelsius(f) + "°C");
        System.out.println(c + "°C = " + converter.celsiusToKelvin(c) + "K");
        System.out.println(k + "K = " + converter.kelvinToCelsius(k) + "°C");
    }
}
