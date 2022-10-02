'''Given string str of length N. The task is to find the minimum characters to be added at the front to make string palindrome.
Note: A palindrome is a word which reads the same backward as forward. Example: "madam".


Input:
S = "abc"
Output: 2
Explanation: 
Add 'b' and 'c' at front of above string to make it
palindrome : "cbabc"


Input:
S = "aacecaaa"
Output: 1
Explanation: Add 'a' at front of above string
to make it palindrome : "aaacecaaa"

You don't need to read input or print anything. Your task is to complete the function minChar() which takes a string S and returns an integer as output.

'''


class Solution:
    def minChar(self,str):
        #Write your code here
        j = len(str)-1
        i = 0
        n = j
        ans = 0
        while(i<j):
            if str[i]==str[j]:
                i+=1
                j-=1
            else:
                ans+=1
                i = 0
                n-=1
                j = n
        return ans


