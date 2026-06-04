#include <iostream>

double calculateBMI(double weight, double height) {
    // Convert height from centimeters to meters
    height /= 100.0;

    // Calculate BMI
    return weight / (height * height);
}

int main() {
    double weight, height;

    std::cout << "Enter weight (in kg): ";
    std::cin >> weight;

    std::cout << "Enter height (in cm): ";
    std::cin >> height;

    double bmi = calculateBMI(weight, height);

    std::cout << "BMI: " << bmi << "\n";

    return 0;
}
