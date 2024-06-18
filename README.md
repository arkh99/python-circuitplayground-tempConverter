# python-circuitplayground-tempConverter
This Python project utilizes the CircuitPlayground board to interactively convert temperature readings between Fahrenheit and Celsius. It integrates user input handling and sensor data processing, showcasing practical use of conditional statements and functions.


Key Features:
Temperature Conversion: Converts temperature readings obtained from CircuitPlayground's onboard sensor between Fahrenheit and Celsius.

User Input Handling: Utilizes input functions to gather user data for temperature conversion.

Interactive Output: Displays converted temperature based on user settings (Fahrenheit or Celsius) and board input (switch status).

Techniques Demonstrated:
Function Definition: Defines functions (CelToFahr, FahrToCel) for temperature conversion, encapsulating logic for reuse and readability.

Conditional Statements: Implements if-else conditions to toggle temperature units (Fahrenheit/Celsius) based on CircuitPlayground switch status and user input.

User Interaction: Incorporates input validation (validateFloat) to ensure correct data type handling for temperature conversion.

Example Usage:
Temperature Conversion: Reads ambient temperature from the CircuitPlayground sensor and converts it to Fahrenheit or Celsius based on user preference.

User Input: Prompts the user for temperature values and validates the input type to prevent errors during conversion.

Interactive Output: Displays the converted temperature value on the CircuitPlayground board's LED matrix or prints it to the console based on user actions (e.g., button presses).
