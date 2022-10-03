/* Abhijeet https://github.com/jacktherock */ 

/* Sort an array with increasing order. While sorting this array return the indexes of array with the increasing order of element...
Size of array: 8
Input: 10 16 7 14 5 3 12 9
Output: 4 7 2 6 1 0 5 3
*/


#include <bits/stdc++.h>
using namespace std;

void file_i_o()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

bool myCompare(pair<int, int> p1, pair<int, int> p2)
{
    return p1.first < p2.first;
}

void Main()
{

    int n;
    cin >> n;
    int arr[n];
    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        v.push_back(make_pair(arr[i], i));
        /* pair<int, int> p;
        p.first = arr[i];
        p.second = i; */
    }
    sort(v.begin(), v.end(), myCompare);
    for (int i = 0; i < n; i++)
    {
        arr[v[i].second] = i;
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    clock_t begin = clock();
    // file_i_o();

    Main();

#ifndef ONLINE_JUDGE
    clock_t end = clock();
    cout << "\n\nExecuted In: " << double(end - begin) / CLOCKS_PER_SEC << " seconds";
#endif

    return 0;
}
