def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

def get_float_input(prompt: str) -> float:
    """Prompt the user for a float input with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to calculate and display BMI."""
    print("Welcome to the BMI Calculator!")
    weight = get_float_input("Enter your weight in kilograms: ")
    height = get_float_input("Enter your height in meters: ")

    if height <= 0 or weight <= 0:
        print("Weight and height must be positive values.")
        return

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()







"""Added Validation for User Input:

The get_float_input function ensures that only valid numerical input is accepted.
Checks for positive values for weight and height.
Enhanced Output Formatting:

BMI is displayed with two decimal places using f"{bmi:.2f}".
Categorized BMI ranges with meaningful messages (underweight, normal weight, etc.).
Code Modularity:

Split the code into functions to enhance readability and reusability.
Added a main() function as the program's entry point, which is a good practice.
Error Handling:

Ensures the program doesn't crash due to invalid inputs.
User Experience:

Added a welcome message and meaningful feedback based on BMI ranges.
This version is more robust, readable, and provides additional features like BMI categorization."""
