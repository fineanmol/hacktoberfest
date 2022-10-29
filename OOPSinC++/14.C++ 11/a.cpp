#include<iostream>
using namespace std;
#include<vector>

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
      
        int size1=sizeof(nums1);
        int size2=sizeof(nums2);
        vector<int>temp;
        int i=0;
        int j=0;
        int l=0;
        while(i<size1 && j<<size2){
            if(nums1[i]<=nums2[j]){
                temp[l]=nums1[i];
                i++;
                l++;
            }else{
                temp[l]=nums2[j];
                j++;
                l++;
            }
        }
        for(;i<size1;i++){
            temp[l++]=nums1[i];
        }
         for(;j<size2;j++){
            temp[l++]=nums2[j];
        }
        if(size1+size2%2==0){
            cout<< (temp[(size1+size2)/2] +temp[(size1+size2+2)/2])/2;
        }else{
            cout<< temp[(size1+size2+1)/2];
        }
    }


int main(){
   vector<int> v1,v2;
   v1.push_back(1);
   v1.push_back(3);
   v1.push_back(5);
   v1.push_back(4);
   v1.push_back(2);
   findMedianSortedArrays(v1,v2);
  
    return 0;
}