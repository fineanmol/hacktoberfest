#include <iostream>
using namespace std;

class Rational
{
private:
    int p;
    int q;

public:
    Rational(int p = 1, int q = 1)
    {
        this->p = p;
        this->q = q;
    }

    friend Rational operator+(Rational r1, Rational r2);
    friend ostream &operator<<(ostream &out, Rational &r);
  
};

Rational operator+(Rational r1, Rational r2)
{
    Rational temp;
    temp.p = (r1.p) * (r2.q) + (r2.p) * (r1.q);
    temp.q = (r1.q) * (r2.q);
    return temp;
}

ostream &operator<<(ostream &out, Rational &r)
{
    out << r.p << "/" << r.q << endl;
}

int main()
{
    Rational r1(3, 4), r2(2, 5), r3;
    r3 = r1 + r2;
    cout<<r3;
    return 0;
}