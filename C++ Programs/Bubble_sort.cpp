// Program to implement the bubble sort technique to sort an array

# include<iostream>
using namespace std;


//  Function to perform Bubble sort technique

void Bubblesort(int arr[], int &size){
    int i, j;
    for(i=0; i<size-1; i++){
        for(j=0; j<size-i-1; j++){
            if(arr[j]>arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

int main(){
    int size, i;
    cout<<"Enter the size of the array : "<<endl;
    cin>>size;

    int *arr = new int [size];  // Create a dynamic array in heap memory
    cout<<"Enter the array elements : "<<endl;
    for(i=0; i<size; i++){
        cin>>arr[i];
    }

    Bubblesort(arr,size);
    cout<<"The sorted array is "<<endl;

    for(i=0; i<size; i++){
        cout<<arr[i];
    }

    delete [] arr;
    return 0;
}
