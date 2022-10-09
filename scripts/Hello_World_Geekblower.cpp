// Language - CPP
// Author - Akash Gautam
// Github - https://github.com/geekblower


#include <bits/stdc++.h>
using namespace std;

// Displaying Hello World using classes and objects
// The code works fine and has been tested
class Greeting {
    private:
      string github_username;
    
    public:
       void setUserName(string github_username) {
         this->github_username = github_username;
       }
  
       void getGreeting() {
        cout<<"Hello World by " << this->github_username;
       }

};

int main(){
   Greeting person1;
   person1.setUserName("Geekblower");
   person1.getGreeting();
   return 0;
}
