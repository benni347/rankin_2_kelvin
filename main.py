def rankine_too_kelvin(temperature_function_param: float) -> str:
    """
    Convert a temperature from Rankine to Kelvin.

    Args:
    temperature_function_param (float): temperature in Rankine.

    Returns:
    str: temperature in Kelvin.

    Example:
    rankine_too_kelvin(491.67) returns "273.15 K".
    """
    return f"{round(temperature_function_param * (5/9), 2)} K"

if __name__ == "__main__":
    temperature = float(input("Please input the temperature in rankin only the int: "))
    temperature = rankine_too_kelvin(temperature)
    print(temperature)
