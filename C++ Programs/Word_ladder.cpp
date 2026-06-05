// LANGUAGE: C++
// AUTHOR: Himanshu Gupta
// GITHUB: https://github.com/himanshugupta11110000
class Solution {
public:
    int ladderLength(string s, string e, vector<string>& a) {
        unordered_set<string> se(a.begin(),a.end());
        if(se.count(e)==0) return 0;
        int lvl=1;
        queue<string> q;
        q.push(s);
        while(!q.empty())
        {
            int size=q.size();
            for(int i=0;i<size;i++)
            {
                string temp=q.front();
                q.pop();
                for(int j=0;j<temp.size();j++)
                {
                    char ori=temp[j];
                    for(char c='a';c<='z';c++)
                    {
                        if(temp[j]==c) continue;
                        temp[j]=c;
                        if(temp==e) return lvl+1;
                        if(se.count(temp))
                        {
                            q.push(temp);
                            se.erase(temp);
                        }
                    }
                    temp[j]=ori; 
                }
            }
            lvl+=1;
        }
        return 0;
    }
};
