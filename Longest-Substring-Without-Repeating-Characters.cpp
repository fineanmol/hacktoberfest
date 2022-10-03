int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for(int i = 0; i <s.size(); i++)
        {
            if(dict[s[i]]> start)
            {
                start = dict[s[i]];
            }
            dict[s[i]] = i;
            maxLen = max(maxLen, i-start);
        }
        return maxLen;
    }
