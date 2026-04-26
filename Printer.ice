module Demo
{
    interface Printer
    {
        // Função original
        string printString(string s);

        // NOVO: inverte a string e a imprime
        string printReversed(string s);

        // NOVO: retorna a string repetida n vezes
        string repeatString(string s, int n);
    }

    // NOVO: objeto servidor para conversão de temperaturas
    interface TemperatureConverter
    {
        // Converte Celsius para Fahrenheit
        float celsiusToFahrenheit(float celsius);

        // Converte Fahrenheit para Celsius
        float fahrenheitToCelsius(float fahrenheit);

        // Converte Celsius para Kelvin
        float celsiusToKelvin(float celsius);
    }
}
