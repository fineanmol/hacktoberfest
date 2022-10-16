#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    long long pow = n;
    double ans = 1.0; 
    if(n<0) pow = -1*pow; 
    while(pow)
    {
        if(pow%2!=0)
        {
            ans*=x; 
            pow--; 
        }
        else
        {
            x*=x; 
            pow/=2; 
        }
          
    }
    if(n<0) return double(1.0)/double(ans);
    return double(ans); 
}


int main()
{
    cout<<myPow(2,5);
    return 0;
}
