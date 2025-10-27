#include <iostream>
#include <cstdlib>  
#include <ctime>   
using namespace std;

int main() {
    srand(time(0)); 
    int userC, computerC;
    cout << "Rock Paper Scissors Game!"<<endl;
    cout << "1. Rock\n2. Paper\n3. Scissors"<<endl;
    cout << "Enter your choice (1-3): ";
    cin >> userC;
    computerC = rand() % 3 + 1;
    cout << "Computer chose: " << computerC << endl;

    if (userC == computerC)
        cout << "It's a tie!" << endl;
    else if ((userC == 1 && computerC == 3)||(userC == 2 && computerC == 1)||(userC == 3 && computerC == 2))
        cout << "You win!" << endl;
    else
        cout << "Computer wins!" << endl;
    return 0;
}
