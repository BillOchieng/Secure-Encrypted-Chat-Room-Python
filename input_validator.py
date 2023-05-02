import re
import json


def validate_input(input_data):
    """
    Validate the input data for financial algorithms
    :param input_data: The input data to validate
    :return: True if the input is valid, False otherwise
    """
    # Define the regular expression pattern for the input data
    pattern = r"^[A-Za-z0-9]*$"

    # Validate the input against the pattern
    if re.match(pattern, input_data):
        return True
    else:
        return False


# Example usage:
input_data = "ABCD1234"
if validate_input(input_data):
    print("Input is valid")
else:
    print("Input is not valid")

# Load the configuration file
with open("config.json", "r") as f:
    config = json.load(f)

# Use the configuration settings
expected_formats = config["expected_formats"]
forbidden_inputs = config["forbidden_inputs"]
