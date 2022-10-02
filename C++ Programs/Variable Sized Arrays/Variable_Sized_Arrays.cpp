#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<vector<int>> arr;
    int n, q, size, val;
    cin >> n >> q;
    for(int i = 0; i < n; i++)
    {
        vector<int> in_arr;
        cin >> size;
        for(int j = 0; j < size; j++)
        {
            cin >> val;
            in_arr.push_back(val);
        }
        arr.push_back(in_arr);
    }
    for(int i = 0; i < q; i++)
    {
        int j, k;
        cin >> j >> k;
        cout << arr[j][k] << endl;
    }
    return 0;
}

// Code Contributed by Preyum Kumar for Anmol Bhai's Repo