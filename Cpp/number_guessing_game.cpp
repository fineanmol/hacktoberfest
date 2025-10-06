#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    // Seed random number generator
    srand(time(0));
    
    // Generate random number between 1 and 100
    int secretNumber = rand() % 100 + 1;
    int guess;
    int attempts = 0;
    
    cout << "================================" << endl;
    cout << "   NUMBER GUESSING GAME" << endl;
    cout << "================================" << endl;
    cout << "I'm thinking of a number between 1 and 100" << endl;
    cout << "Can you guess it?" << endl << endl;
    
    // Game loop
    do {
        cout << "Enter your guess: ";
        cin >> guess;
        attempts++;
        
        if (guess > secretNumber) {
            cout << "Too high! Try again." << endl << endl;
        }
        else if (guess < secretNumber) {
            cout << "Too low! Try again." << endl << endl;
        }
        else {
            cout << "\n*** CONGRATULATIONS! ***" << endl;
            cout << "You guessed the number in " << attempts << " attempts!" << endl;
            
            // Rating based on attempts
            if (attempts <= 5) {
                cout << "Excellent! You're a guessing master!" << endl;
            }
            else if (attempts <= 10) {
                cout << "Good job! Nice guessing!" << endl;
            }
            else {
                cout << "You got it! Keep practicing!" << endl;
            }
        }
        
    } while (guess != secretNumber);
    
    cout << "\nThanks for playing!" << endl;
    
    return 0;
}
