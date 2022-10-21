class Solution {
public:
    string convert(string s, int row) {
        if(row==1){
            return s;
        }
        vector<string>nums(row);
        bool down= false;
        int j=0;
        for(int i=0;i<s.size();i++){
            nums[j].push_back(s[i]);
            if(j==row-1){
                down=false;
            }
            else if(j==0){
                down=true;
            }
            if(down==true){
                j++;
            }
            else j--;
        }
    string ans="";
    for(auto i:nums){
        ans+=i;
    }
        return ans;
}
};