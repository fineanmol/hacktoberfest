// LANGUAGE: C++
// ENV: Node.js
// AUTHOR: Sushant Khadka
// GITHUB: https://github.com/NameLesssNerd

#include <iostream>
#include <string.h>
using namespace std;

class Banking
{
private:
    int accountNumber, currentBalance, deposite, withdraw, garbageCollector, choiceData, pin, repin, loginChance, loginPin, accountCheck, userlogin, sessionPin, sessionAccount, userID, userIDInitial;
    char name[20];
    bool Exit = true;
    bool exitUser = true;

public:
    Banking();
    Banking(Banking, Banking, Banking, Banking, Banking, Banking, Banking, Banking, Banking, Banking);

    // ---- setDetails-----------
    void setDetails(int acc, int curren, int p, int rep, const char *n)
    {
        accountNumber = acc;
        currentBalance = curren;
        pin = p;
        repin = rep;
        strcpy(name, n);
    }

    //------------Display Section-------------------
    void displaySingleDetails(Banking &b)
    {
        cout << endl
             << "NAME : " << b.name << endl
             << "ACCOUNT NUMBER : " << b.accountNumber << endl
             << "CURRENT BALANCE : " << b.currentBalance << endl;
    }
    void displayAllData(Banking &b1, Banking &b2, Banking &b3, Banking &b4, Banking &b5, Banking &b6, Banking &b7, Banking &b8, Banking &b9, Banking &b10)
    {
        Banking word[40] = {b1, b2, b3, b4, b5, b6, b7, b8, b9, b10};
        for (int i = 0; i <= 9; i++)
        {
            cout << endl
                 << "NAME : " << word[i].name << endl
                 << "ACCOUNT NUMBER : " << word[i].accountNumber << endl
                 << "CURRENT BALANCE : " << word[i].currentBalance << endl
                 << "PIN : " << word[i].pin << endl;
        }
    }

    void displayChoice()
    {
        cout << endl
             << "+------------------- Main Menu --------------------+" << endl;
        cout << "|    1. Display Details                            |" << endl;
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    2. Login                                      |" << endl;
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    3. Exit                                       |" << endl;
        cout << "+--------------------------------------------------+" << endl;
    }

    //----------Input Taking section------------------
    void loginChoiceUser()
    {
        cout << "Enter Your Options: ";
        cin >> userlogin;
    }
    int userChoice()
    {
        int choice;
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    Enter Your Choice  :  ";
        cin >> choice;
        cout << "+--------------------------------------------------+" << endl;
        choiceData = choice;
        return choice;
    }
    int returnObjValue()
    {
        return userIDInitial;
    }

    // ----- Value assiginig section-------
    void assignSessionValue(Banking b1, Banking b2, Banking b3, Banking b4, Banking b5, Banking b6, Banking b7, Banking b8, Banking b9, Banking b10)
    {
        Banking word[40] = {b1, b2, b3, b4, b5, b6, b7, b8, b9, b10};
        for (int i = 0; i < 10; i++)
        {
            if (word[i].accountNumber == sessionAccount)
            {
                sessionPin = word[i].pin;
                userIDInitial = i;
            }
        }
    }

    // ------- Calculation section--------
    void depositeAmount(Banking &b)
    {
        cout << "Enter the Amount to deposite : ";
        cin >> deposite;
        b.currentBalance += deposite;
    }

    void withdrawAmount(Banking &b)
    {
        cout << "Enter the Amount to withdraw : ";
        cin >> withdraw;
        if ((b.currentBalance > 0) && (b.currentBalance >= withdraw))
        {
            b.currentBalance -= withdraw;
            cout << "\n\n+--------------------------------------------------+" << endl;
            cout << "|    Withdraw sucessfull                           |" << endl;
            cout << "+--------------------------------------------------+" << endl;
        }
        else
        {
            cout << "\n\n+--------------------------------------------------+" << endl;
            cout << "|    Sorry not Enough Balance                      |" << endl;
            cout << "+--------------------------------------------------+" << endl;
        }
    }

    // ------------ Logic Check section--------------

    void userLogin(Banking &b1, Banking &b2, Banking &b3, Banking &b4, Banking &b5, Banking &b6, Banking &b7, Banking &b8, Banking &b9, Banking &b10)
    {
        cout << "\n+--------------------------------------------------+" << endl;
        cout << "|    Enter Your Account Here  :                   ";
        cin >> sessionAccount;
        cout << "+--------------------------------------------------+" << endl;
        assignSessionValue(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10);
        cout << "\n+--------------------------------------------------+" << endl;
        cout << "|    Enter Your Pin Here  :                        ";
        cin >> loginPin;
        cout << "+--------------------------------------------------+" << endl;
        while (loginChance != 0)
        {

            if (loginPin == sessionPin)
            {
                loginMessage();
                mainLogin(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10);
                logoutMessage();
                break;
            }
            else
            {
                incorrectPin();
                loginChance--;
                cout << "\n+--------------------------------------------------+" << endl;
                cout << "|    Enter Your Pin Here  :                        ";
                cin >> loginPin;
                cout << "+--------------------------------------------------+" << endl;
                if (loginChance == 0)
                {
                    break;
                }
            }
        }
    }
    void mainLogin(Banking &b1, Banking &b2, Banking &b3, Banking &b4, Banking &b5, Banking &b6, Banking &b7, Banking &b8, Banking &b9, Banking &b10)
    {
        Banking word[40] = {b1, b2, b3, b4, b5, b6, b7, b8, b9, b10};
        userID = returnObjValue();
        while (exitUser)
        {
            displayMenu();
            if (choiceData == 1)
            {
                displaySingleDetails(word[userID]);
            }
            else if (choiceData == 2)
            {
                depositeAmount(word[userID]);
            }
            else if (choiceData == 3)
            {
                withdrawAmount(word[userID]);
            }
            else if (choiceData == 4)
            {
                ExitUser();
            }
            else
            {
                errorMessage();
            }
        }
    }
    // ------- Message Show sesction--------
    void displayMenu()
    {
        cout << endl
             << "+------------------- Main Menu --------------------+" << endl;
        cout << "|    1. Display Details                            |" << endl;
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    2. Deposite Amount                            |" << endl;
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    3. Withdraw Amount                            |" << endl;
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    4. Exit                                       |" << endl;
        cout << "+--------------------------------------------------+" << endl;
        choiceData = userChoice();
    }
    void logoutMessage()
    {
        cout << "\n+--------------------------------------------------+" << endl;
        cout << "|    Logout Sucessfully                            |" << endl;
        cout << "+--------------------------------------------------+" << endl;
    }
    void incorrectPin()
    {
        cout << "+--------------------------------------------------+" << endl;
        cout << "|    Incorrect Pin                                 |" << endl;
        cout << "+--------------------------------------------------+" << endl;
    }
    void loginMessage()
    {
        cout << "\n+--------------------------------------------------+" << endl;
        cout << "|    Login Sucessfully                             |" << endl;
        cout << "+--------------------------------------------------+" << endl;
    }
    void exitBank()
    {
        Exit = false;
    }
    void ExitUser()
    {
        exitUser = false;
    }
    void errorMessage()
    {
        cout << endl
             << endl
             << "+--------------------------------------------------+" << endl;
        cout << "|    Inalid choice                                 |" << endl;
        cout << "+--------------------------------------------------+" << endl
             << endl;
    }
};
Banking::Banking()
{
    userID = 0;
    accountNumber = 0;
    currentBalance = 0;
    deposite = 0;
    withdraw = 0;
    pin = 0;
    repin = 0;
    loginChance = 2;
    sessionPin = 0;
    sessionAccount = 0;
}
Banking::Banking(Banking b1, Banking b2, Banking b3, Banking b4, Banking b5, Banking b6, Banking b7, Banking b8, Banking b9, Banking b10)
{
    while (Exit)
    {
        displayChoice();
        loginChoiceUser();
        if (userlogin == 1)
        {
            displayAllData(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10);
            displayChoice();
        }
        else if (userlogin == 2)
        {
            userLogin(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10);
        }
        else if (userlogin == 3)
        {
            exitBank();
        }
        else
        {
            errorMessage();
        }
    }
}
int main()
{
    Banking U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10;
    U1.setDetails(123, 4000, 900, 900, "Sushant Khadka");
    U2.setDetails(3445, 10000, 100, 100, "Avanish Duwadi");
    U3.setDetails(4645, 9000, 200, 200, "Dayaram Dahal");
    U4.setDetails(4845, 800, 400, 400, "Hari Bansha Acharya");
    U5.setDetails(4945, 100, 800, 800, "Subash Gajurel");
    U6.setDetails(4905, 100, 1900, 1900, "Tulsi Ghimire");
    U7.setDetails(415, 600, 2300, 2300, "Manisha Koirala");
    U8.setDetails(145, 300, 9900, 9900, "Nischal Basnet");
    U9.setDetails(745, 200, 7700, 7700, "Priyanka Karki");
    U10.setDetails(75, 9000, 4500, 4500, "Saugat Malla");
    Banking All(U1, U2, U3, U4, U5, U6, U7, U8, U9, U10);
    return 0;
}