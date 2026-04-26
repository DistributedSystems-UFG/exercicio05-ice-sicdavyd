import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

# --- Objeto Printer ---
base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

# Função original
printer.printString("Hello World!")

# NOVO: imprime a string invertida
reversed_s = printer.printReversed("Hello World!")
print(f"Invertida: {reversed_s}")

# NOVO: imprime a string repetida 3 vezes
repeated = printer.repeatString("Ice", 3)
print(f"Repetida: {repeated}")

# --- NOVO objeto TemperatureConverter ---
base_conv = communicator.stringToProxy("SimpleConverter:default -p 11000")
converter = Demo.TemperatureConverterPrx.checkedCast(base_conv)
if not converter:
    raise RuntimeError("Invalid proxy")

# NOVO: converte Celsius para Fahrenheit
f = converter.celsiusToFahrenheit(100.0)
print(f"100°C em Fahrenheit: {f:.2f}°F")

# NOVO: converte Fahrenheit para Celsius
c = converter.fahrenheitToCelsius(212.0)
print(f"212°F em Celsius: {c:.2f}°C")

# NOVO: converte Celsius para Kelvin
k = converter.celsiusToKelvin(0.0)
print(f"0°C em Kelvin: {k:.2f}K")
