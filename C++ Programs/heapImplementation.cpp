#include <iostream>
using namespace std;

class heap
{

public:
    int arr[100];
    int size;

    heap()
    {
        arr[0] = -1;
        size = 0;
    }

    void insert(int data)
    {

        size++;
        int index = size;
        arr[index] = data;

        while (index > 1)
        {
            int parent = index / 2;
            if (arr[parent] < arr[index])
            {
                swap(arr[parent], arr[index]);
                index = parent;
            }
            else
            {
                return;
            }
        }
    }

    void print()
    {
        for (int i = 1; i <= size; i++)
        {
            cout << arr[i] << " -> ";
        }cout<<endl ;
    }

    void deleteFromHeap()
    {

        arr[1] = arr[size];
        size--;

        int i = 1;

        while (i < size)
        {
            int left = 2 * i;
            int right = 2 * i + 1;

            if (left < size && arr[left] > arr[i])
            {
                swap(arr[left], arr[i]);
                i = left;
            }
            else if (right < size && arr[right] > arr[i])
            {
                swap(arr[right], arr[i]);
                i = right;
            }
            else
            {
                return;
            }
        }
    }
};

void heapify(int arr[] , int size , int i){
    int largest = i ;
    int left = 2*i ;
    int right = 2*i+1 ;

    if(left < size && arr[left] > arr[largest]){
        largest = left ;
    }
    if(right < size && arr[right] > arr[largest]){
        largest = right ;
    }
  
    if(largest != i){
        swap( arr[i] , arr[largest] ) ;
        heapify(arr,size,largest) ;    
    }

}

void heapSort(int arr[] , int n){                                       
    for (int i = n/2; i > 0; i--){                                       
        heapify(arr,n,i) ;                                       
    }    
    for (int i = 1; i <= n; i++){
        cout<<arr[i]<<" " ;
    } cout<<endl ;        
    int t=n ;                           
                                       
    while(t>1){                                       
        swap(arr[1] , arr[t]) ;                                       
        t-- ;                                       
        heapify(arr,t,1) ;                                       
    }  

    for (int i = 1; i <= n; i++){
        cout<<arr[i]<<" " ;
    }                                   
}                                       
                                       
int main()                                       
{                                       
                                       
    // heap h1;                                       
    // h1.insert(50);                                       
    // h1.insert(55);                                       
    // h1.insert(53);                                       
    // h1.insert(52);                                       
    // h1.insert(54);                                       
    // h1.print();                                       
    // h1.deleteFromHeap() ;                                        
    // h1.print();                                       
                                       
    int arr[6] = {-1, 60 , 50 , 55 ,45 ,70} ;                                       
    int n=5 ;                                       
    // for (int i = 1; i <= n; i++)                                       
    // {                                       
    //     cout<<arr[i]<<" " ;                                       
    // }                                       
                                       
    // for (int i = n/2; i > 0; i--)
    // {
    //     heapify(arr,n,i) ;
    // }cout<<endl ;

    // for (int i = 1; i <= n; i++)
    // {
    //     cout<<arr[i]<<" " ;
    // }

    // cout<<endl ;

    heapSort(arr,n) ;


    return 0;
}