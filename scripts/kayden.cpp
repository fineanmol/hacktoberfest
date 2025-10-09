#include <iostream>
#include <vector>
#include <climits> // for INT_MIN
using namespace std;

int main()
{
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
    int maxs = INT_MIN;
    int current = 0;

    for (int i = 0; i < v.size(); i++)
    {
        current += v[i];
        maxs = max(maxs, current);

        // reset if current sum goes negative
        if (current < 0)
            current = 0;
    }

    cout << "Maximum subarray sum = " << maxs << endl;
    return 0;
}
