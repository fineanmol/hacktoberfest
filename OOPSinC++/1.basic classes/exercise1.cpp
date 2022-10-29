#include <iostream>
#include <cstring>
using namespace std;

class Student
{
private:
    string name;
    int roll_number;
    int Phy_marks;
    int Chem_marks;
    int Maths_marks;

public:
    Student(string name, int roll_number, int Phy_marks, int Chem_marks, int Maths_marks)
    {
        this->name = name;
        this->roll_number = roll_number;
        this->Phy_marks = Phy_marks;
        this->Chem_marks = Chem_marks;
        this->Maths_marks = Maths_marks;
    };

    int total()
    {
        return Phy_marks + Chem_marks + Maths_marks;
    };
    
    char Grade()
    {
        if (total() >= 225)
        {
            return 'A';
        }
        if (total() >= 200)
        {
            return 'B';
        }
        if (total() >= 175)
        {
            return 'C';
        }
        if (total() >= 150)
        {
            return 'D';
        }
        if (total() >= 125)
        {
            return 'E';
        }
        if (total() < 125)
        {
            return 'F';
        }
    }
};

int main()
{
    string name;
    int roll_number;
    int Phy_marks, Chem_marks, Maths_marks;
    cout << "Enter student name: " << endl;
    cin >> name;
    cout << "Enter Roll Number" << endl;
    cin >> roll_number;
    cout << "Enter marks for Physics: " << endl;
    cin >> Phy_marks;
    cout << "Enter marks for Chemistry: " << endl;
    cin >> Chem_marks;
    cout << "Enter marks for Maths: " << endl;
    cin >> Maths_marks;

    Student S(name, roll_number, Phy_marks, Chem_marks, Maths_marks);
    cout << "Total Marks: " << S.total() << endl;
    cout << "Grade: " << S.Grade() << endl;
    return 0;
}