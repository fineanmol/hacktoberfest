#include <iostream>
#include <algorithm>
using namespace std;

int linearSearch(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
            return i;
    }

    return -1;
}

int binarySearch(int arr[], int n, int key)
{
    int s = 0;
    int e = n - 1;

    while (s <= e)
    {
        int mid = s + (e - s) / 2;

        if (arr[mid] == key)
        {
            return mid;
        }
        else if (arr[mid] < key)
        {
            s = mid + 1;
        }
        else
        {
            e = mid - 1;
        }
    }
    return -1;
}

int main()
{
    int arr[100];
    cout << "Enter the size of the array" << endl;

    int n;
    cin >> n;
    cout << "Enter the elments in array" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Enter the key to be searched" << endl;
    int key;
    cin >> key;

    cout << linearSearch(arr, n, key) << endl;
    sort(arr, arr + n);
    cout << binarySearch(arr, n, key) << endl;
    return 0;
}