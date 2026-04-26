import sys, Ice
import Demo


class PrinterI(Demo.Printer):

    # Função original
    def printString(self, s, current=None):
        print(s)
        return s

    # NOVO: inverte a string e a imprime
    def printReversed(self, s, current=None):
        reversed_s = s[::-1]
        print(reversed_s)
        return reversed_s

    # NOVO: repete a string n vezes e a imprime
    def repeatString(self, s, n, current=None):
        repeated = (s + " ") * n
        print(repeated)
        return repeated


# --- NOVO objeto TemperatureConverter ---
class TemperatureConverterI(Demo.TemperatureConverter):

    def celsiusToFahrenheit(self, celsius, current=None):
        return celsius * 9.0 / 5.0 + 32.0

    def fahrenheitToCelsius(self, fahrenheit, current=None):
        return (fahrenheit - 32.0) * 5.0 / 9.0

    def celsiusToKelvin(self, celsius, current=None):
        return celsius + 273.15


communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")

printer = PrinterI()
adapter.add(printer, communicator.stringToIdentity("SimplePrinter"))

# NOVO: registra o TemperatureConverter com a identidade "SimpleConverter"
converter = TemperatureConverterI()
adapter.add(converter, communicator.stringToIdentity("SimpleConverter"))

adapter.activate()

communicator.waitForShutdown()
