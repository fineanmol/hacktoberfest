#include <iostream>
using namespace std;

void swapping(int &a, int &b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void merge(int *arr, int l, int m, int r)
{
    int i, j, k, nl, nr;
    nl = m - l + 1;
    nr = r - m;
    int l[nl], r[nr];
    for (i = 0; i < nl; i++)
        l[i] = arr[l + i];
    for (j = 0; j < nr; j++)
        r[j] = arr[m + 1 + j];
    i = 0;
    j = 0;
    k = l;
    while (i < nl && j < nr)
    {
        if (l[i] <= r[j])
        {
            arr[k] = l[i];
            i++;
        }
        else
        {
            arr[k] = r[j];
            j++;
        }
        k++;
    }
    while (i < nl)
    {
        arr[k] = l[i];
        i++;
        k++;
    }
    while (j < nr)
    {
        arr[k] = r[j];
        j++;
        k++;
    }
}

void mergeSort(int *arr, int l, int r)
{
    int m;
    if (l < r)
    {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void printArray(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
        cout << endl;
    }
}

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int arr[n];
    cout << "Enter elements:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Array before Sorting: ";
    printArray(arr, n);
    mergeSort(arr, 0, n - 1);
    cout << "Array after Sorting: ";
    printArray(arr, n);
}