#include <iostream>
#include <vector>

// Merge two subarrays of arr[].
// First subarray is arr[l..m], and the second subarray is arr[m+1..r].
void merge(std::vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temporary arrays to store the two subarrays.
    std::vector<int> left(n1);
    std::vector<int> right(n2);

    // Copy data to temporary arrays left[] and right[].
    for (int i = 0; i < n1; i++)
        left[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[m + 1 + j];

    // Merge the temporary arrays back into arr[l..r].
    int i = 0;
    int j = 0;
    int k = l;
    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of left[], if any.
    while (i < n1) {
        arr[k] = left[i];
        i++;
        k++;
    }

    // Copy the remaining elements of right[], if any.
    while (j < n2) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// Main function to perform merge sort on arr[].
void mergeSort(std::vector<int>& arr, int l, int r) {
    if (l < r) {
        // Find the middle point of the array.
        int m = l + (r - l) / 2;

        // Recursively sort the first and second halves.
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        // Merge the sorted halves.
        merge(arr, l, m, r);
    }
}

int main() {
    std::vector<int> arr = {12, 11, 13, 5, 6, 7};

    std::cout << "Original Array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    int n = arr.size();

    mergeSort(arr, 0, n - 1);

    std::cout << "Sorted Array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
