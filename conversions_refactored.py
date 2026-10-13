class ConversionNotPossible(Exception):
    """Raised when a conversion between units is not possible."""
    pass


def convert(fromUnit, toUnit, value):
    """Convert between compatible temperature or distance units."""

    temperature_units = ("C", "F", "K")

    distance_units = {
        "Miles": 1609.344,
        "Yards": 0.9144,
        "Meters": 1.0
    }

    # Check that the units are compatible.
    if fromUnit in temperature_units and toUnit in temperature_units:

        if fromUnit == toUnit:
            return float(value)

        # Convert the original temperature to Celsius.
        if fromUnit == "C":
            celsius = value
        elif fromUnit == "F":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        # Convert Celsius to the requested temperature unit.
        if toUnit == "C":
            result = celsius
        elif toUnit == "F":
            result = celsius * 9 / 5 + 32
        else:
            result = celsius + 273.15

        return float(result)

    elif fromUnit in distance_units and toUnit in distance_units:

        # Convert the original distance to meters.
        meters = value * distance_units[fromUnit]

        # Convert meters into the requested distance unit.
        result = meters / distance_units[toUnit]

        return float(result)

    else:
        raise ConversionNotPossible(
            f"Cannot convert from {fromUnit} to {toUnit}"
        )