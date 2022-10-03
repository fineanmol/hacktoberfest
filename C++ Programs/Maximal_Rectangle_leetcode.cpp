// LANGUAGE: C++
// AUTHOR: Himanshu Gupta
// GITHUB: https://github.com/himanshugupta11110000
class Solution {
public:
    void Nearest_smallest_left(vector<int>& nsl,vector<int> & arr){
        stack<int> st;
        for(int i=0;i<arr.size();i++){
            while(!st.empty() && arr[i]<=arr[st.top()])
                st.pop();
            if(st.empty())
                nsl.push_back(-1);
            else
                nsl.push_back(st.top());

            st.push(i);
        }
    }

    void Nearest_smallest_right(vector<int>& nsr,vector<int> & arr){
        stack<int> st;
        for(int i=arr.size()-1;i>=0;i--){
            while(!st.empty() && arr[i]<=arr[st.top()])
                st.pop();

            if(st.empty())
                nsr.push_back(arr.size());
            else 
                nsr.push_back(st.top());

            st.push(i);
        }
        reverse(nsr.begin(),nsr.end());
    } 


    int largestRectangleArea(vector<int>& heights) {
        vector<int> nsl;  
        vector<int> nsr; 
        Nearest_smallest_left(nsl,heights);
        Nearest_smallest_right(nsr,heights);

        int ans=0;
        int area=0;


        for(int i=0;i<heights.size();i++){
            area=heights[i]*(nsr[i]-nsl[i]-1);
            if(ans<area)
                ans=area;
        }

        return ans;

    }
    int maximalRectangle(vector<vector<char>>& mat) {
         if(mat.empty())
    {
        return 0;
    }
        vector<int> v(mat[0].size(),0);
        int maxx=INT_MIN;
        for(int i=0;i<mat.size();i++)
        {
            for(int j=0;j<mat[0].size();j++)
            {
                if(mat[i][j]=='1') v[j]+=mat[i][j]-'0';
                else v[j]=0;
            }
            maxx=max(maxx,largestRectangleArea(v));
        }
        return maxx;

    }
};
