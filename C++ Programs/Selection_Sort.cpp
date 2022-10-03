// Program to implement the Selection sort technique to sort an array

#  include<iostream>
using namespace std;

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = *a;
}

void selectionSort(int arr[], int &size){
    int i, j;
    for(i = 0; i<size-1; i++){
        int min = i;
        for(j = i+1; j<size; j++){
            if(arr[j]<arr[min]){
            min  = j;
        }
        }
         swap(arr[min], arr[i]);
    }
}

int main(){
    int size, i;
    cout<<"Enter the size of the array : "<<endl;
    cin>>size;

    int *arr = new int[size];

    cout<<"Enter the array elements : "<<endl;

    for(i=0; i<size; i++){
        cin>>arr[i];
    }

    selectionSort(arr, size);

    cout<<"<--------- The sorted array is -------->"<<endl;

    for(i=0; i<size; i++){
        cout<<arr[i]<<endl;
    } 

    return 0;
}