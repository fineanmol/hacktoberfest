#include<iostream>
#include<string>
using namespace std;
int main(){
    int arr1[] = {1,2,3,98,5,6};
    bool swap=false;
    for(int i=0;i<6;i++){
        for(int j=0;j-i;j++){
            int temp;
            
                if((arr1[j]>arr1[j+1])&&swap==false){
                    temp = arr1[j];
                    arr1[j]=arr1[j+1];
                    arr1[j+1]=temp;
                    swap = true;
                    

            

            }
            
        }
        swap = false;
    }

    for(int i = 0; i < 6; i++)
{
    cout<<arr1[i];
}




    

}


