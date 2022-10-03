/* Abhijeet https://github.com/jacktherock */ 

#include <bits/stdc++.h>
using namespace std;

void file_i_o()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

void Main()
{
    int n;
    cin >> n;
    cin.ignore();

    char arr[n + 1];
    cin.getline(arr, n);
    cin.ignore();

    int i = 0;
    int currLen = 0, maxLen = 0;
    int start = 0, maxStart = 0;
    while (1)
    {
        if (arr[i] == ' ' || arr[i] == '\0')
        {
            if (currLen > maxLen)
            {
                maxLen = currLen;
                maxStart = start;
            }
            currLen = 0;
            start = i + 1;
        }
        else
        {
            currLen++;
        }
        if (arr[i] == '\0')
        {
            break;
        }
        i++;
    }

    cout << maxLen << endl;
    for (int i = 0; i < maxLen; i++)
    {
        cout << arr[i + maxStart];
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

/* Input
17
I am jacktherock
*/