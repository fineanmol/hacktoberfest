# LANGUAGE: Python
# ENV: Python
# AUTHOR: Ratheshan Sathiyamoorthy
# GITHUB: https://github.com/Ratheshan03

import colorama
# Install ->  pip install colorama
from colorama import Fore, Back, Style

# Initialize colorama for colored output
colorama.init(autoreset=True)

# Define the message and formatting
message = "Hello, World!"
formatted_message = f"{Fore.GREEN}{Style.BRIGHT}{Back.BLACK}{message}{Style.RESET_ALL}"

# Print the fancy "Hello, World!" message
print(formatted_message)
