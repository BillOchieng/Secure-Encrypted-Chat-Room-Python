# import argparse
# import csv
# import json
# import re


# def validate_input(input_data, expected_formats):
#     """
#     Validate the input data based on expected formats defined in the configuration file
#     :param input_data: The input data to validate
#     :param expected_formats: List of dictionaries containing name and format of expected inputs
#     :return: True if the input is valid, False otherwise
#     """
#     # Validate the input against the expected formats
#     for expected_format in expected_formats:
#         if expected_format["name"] in input_data:
#             if re.match(expected_format["format"], input_data):
#                 return True
#             else:
#                 print(
#                     f"Invalid input for {expected_format['name']}. Expected format: {expected_format['format']}"
#                 )
#                 return False
#     return True


# def main(config_file, input_file, output_file):
#     # Load the configuration file
#     with open(config_file, "r") as f:
#         config = json.load(f)

#     # Use the configuration settings
#     expected_formats = config["expected_formats"]
#     forbidden_inputs = config["forbidden_inputs"]

#     # Read the input data file
#     with open(input_file, "r") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             for input_data in row:
#                 # Validate the input data
#                 if validate_input(input_data, expected_formats):
#                     print(f"{input_data} is valid")
#                 else:
#                     # Check for forbidden inputs
#                     for forbidden_input in forbidden_inputs:
#                         if forbidden_input in input_data:
#                             print(
#                                 f"Found forbidden input {forbidden_input} in {input_data}"
#                             )
#                             break

#     # Write the results to the output file
#     with open(output_file, "w") as f:
#         f.write("Results\n")


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description="Scan financial algorithms for vulnerabilities"
#     )
#     parser.add_argument(
#         "--config", type=str, required=True, help="Path to the configuration file"
#     )
#     parser.add_argument(
#         "--input", type=str, required=True, help="Path to the input data file"
#     )
#     parser.add_argument(
#         "--output", type=str, required=True, help="Path to the output file"
#     )
#     args = parser.parse_args()

#     main(args.config, args.input, args.output)

import argparse
import csv
import json
import re


def validate_input(input_data, expected_formats):
    """
    Validate the input data based on expected formats defined in the configuration file
    :param input_data: The input data to validate
    :param expected_formats: List of dictionaries containing name and format of expected inputs
    :return: True if the input is valid, False otherwise
    """
    # Validate the input against the expected formats
    for expected_format in expected_formats:
        if expected_format["name"] in input_data:
            if re.match(expected_format["format"], input_data):
                return True
            else:
                print(
                    f"Invalid input for {expected_format['name']}. Expected format: {expected_format['format']}"
                )
                return False
    return True


def main():
    # Prompt the user to enter the file paths
    config_file = input("Enter the path to the configuration file: ")
    input_file = input("Enter the path to the input data file: ")
    output_file = input("Enter the path to the output file: ")

    # Load the configuration file
    with open(config_file, "r") as f:
        config = json.load(f)

    # Use the configuration settings
    expected_formats = config["expected_formats"]
    forbidden_inputs = config["forbidden_inputs"]

    # Read the input data file
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for input_data in row:
                # Validate the input data
                if validate_input(input_data, expected_formats):
                    print(f"{input_data} is valid")
                else:
                    # Check for forbidden inputs
                    for forbidden_input in forbidden_inputs:
                        if forbidden_input in input_data:
                            print(
                                f"Found forbidden input {forbidden_input} in {input_data}"
                            )
                            break

    # Write the results to the output file
    with open(output_file, "w") as f:
        f.write("Results\n")


if __name__ == "__main__":
    main()
