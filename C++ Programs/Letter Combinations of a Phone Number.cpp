class Solution {
public:
    string buttons[10] = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    vector<string> ans;
    
    void helper(string& digits,int index,string &tmp) {
        if(index==digits.size()) {
            if(tmp!="")ans.push_back(tmp);
            return;
        }
        int bi=digits[index]-'0';
        for(int i=0;i<buttons[bi].size();i++) {
            tmp.push_back(buttons[bi][i]);
            helper(digits,index+1,tmp);
            tmp.pop_back();
        }
    }
    
    vector<string> letterCombinations(string digits) {
        string tmp="";
        helper(digits,0,tmp);
        return ans;
    }
};
