import unittest
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)
from conversions_refactored import (
    convert,
    ConversionNotPossible
)

class TestConversions(unittest.TestCase):
    def test_Celsius_To_Kelvin(self):
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-273.15, 0),
            (300, 573.15),
            (-40, 233.15)
        ]

        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"{celsius} C = {result} K")
            self.assertAlmostEqual(result, expected)
            
    def test_Celsius_To_Fahrenheit(self):
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (300, 572),
            (-273.15, -459.67)
        ]

        for celsius, expected in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"{celsius} C = {result} F")
            self.assertAlmostEqual(result, expected)

    def test_Fahrenheit_To_Celsius(self):
        test_cases = [
            (32, 0),
            (212, 100),
            (-40, -40),
            (98.6, 37),
            (50, 10)
        ]

        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            print(f"{fahrenheit} F = {result} C")
            self.assertAlmostEqual(result, expected)

    def test_Fahrenheit_To_Kelvin(self):
        test_cases = [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (-459.67, 0),
            (98.6, 310.15)
        ]

        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            print(f"{fahrenheit} F = {result} K")
            self.assertAlmostEqual(result, expected)

    def test_Kelvin_To_Celsius(self):
        test_cases = [
            (273.15, 0),
            (373.15, 100),
            (233.15, -40),
            (0, -273.15),
            (300, 26.85),            
        ]

        for kelvin, expected in test_cases:
            result = convertKelvinToCelsius(kelvin)
            print(f"{kelvin} K = {result} C")
            self.assertAlmostEqual(result, expected)

    def test_Kelvin_To_Fahrenheit(self):
        test_cases = [
            (273.15, 32),
            (373.15, 212),
            (233.15, -40),
            (0, -459.67),
            (310.15, 98.6)
        ]

        for kelvin, expected in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            print(f"{kelvin} K = {result} F")
            self.assertAlmostEqual(result, expected)

class TestRefactoredConversions(unittest.TestCase):
    def test_convert(self):
        test_cases = [
            ('C', 'K', 0, 273.15),
            ('C', 'F', 100, 212),
            ('F', 'C', 32, 0),
            ('F', 'K', 212, 373.15),
            ('K', 'C', 273.15, 0),
            ('K', 'F', 373.15, 212)
        ]

        for fromUnit, toUnit, value, expected in test_cases:
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                result = convert(fromUnit, toUnit, value)            
                self.assertAlmostEqual(result, expected)

    def test_distance_conversions(self):
        test_cases = [
            ("Miles", "Yards", 1, 1760),
            ("Yards", "Miles", 1760, 1),
            ("Miles", "Meters", 1, 1609.344),
            ("Meters", "Miles", 1609.344, 1),
            ("Yards", "Meters", 1, 0.9144),
            ("Meters", "Yards", 0.9144, 1)
        ]

        for fromUnit, toUnit, value, expected in test_cases:
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                result = convert(fromUnit, toUnit, value)
                print(f"{value} {fromUnit} = {result} {toUnit}")
                self.assertAlmostEqual(result, expected)

    def test_same_unit_conversions(self):
        test_cases = [
            ("C", 100),
            ("F", 32),
            ("K", 273.15),
            ("Miles", 5),
            ("Yards", 100),
            ("Meters", 250)
        ]

        for unit, value in test_cases:
            with self.subTest(unit=unit):
                result = convert(unit, unit, value)
                print(f"{value} {unit} = {result} {unit}")
                self.assertAlmostEqual(result, value)
    
    def test_incompatible_conversions(self):
        test_cases = [
            ("C", "Miles", 100),
            ("F", "Meters", 32),
            ("K", "Yards", 273.15),
            ("Miles", "C", 5),
            ("Yards", "F", 100),
            ("Meters", "K", 250)
        ]

        for fromUnit, toUnit, value in test_cases:
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                with self.assertRaises(ConversionNotPossible):
                    convert(fromUnit, toUnit, value)
                    

if __name__ == '__main__':
    unittest.main()