#include<iostream>
#include<cstring>
using namespace std;

class Employee{
    private:
    string name;
    int id;

    public:
    Employee(string name,int id){
        this->name=name;
        this->id=id;
    }
    void setName(string n){
        name=n;
    }

    void setId(int id){
        this->id=id;
    }

    string getName(){
        return name;
    }

    int getId(){
        return id;
    }

};

class FulltimeEmployee :public Employee{
    private:
    int fulltime_salary;

    public:
    //note.. you can inherit Constructor function too
    FulltimeEmployee(string name,int id,int sal) : Employee(name,id){
        fulltime_salary=sal;
    }

    void setfulltimeSalary(int f){
        fulltime_salary=f;
    }

    int getSalary(){
        return fulltime_salary;
    }
};

class ParttimeEmployee : public Employee{
    private:
    int partTime_salary;

    public:
    ParttimeEmployee(string name,int id, int sal) : Employee(name,id){
        partTime_salary=sal;
    }
    void setpartTimeSalary(int p){
        partTime_salary=p;
    }

    int getWage(){
        return partTime_salary;
    }
};

int main()
{
    FulltimeEmployee e1("Utk",48,250000);
    cout<<"Salary of "<<e1.getName()<<" is "<<e1.getSalary()<<endl;
    ParttimeEmployee e2("Mann",16,500);
    cout<<"Daily wage of "<<e2.getName()<<" is "<<e2.getWage();
    return 0;
}