#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=d[S[len(S)-1]]
        for i in range(len(S)-1):
            if(d[S[i]]<d[S[i+1]]):
                res-=d[S[i]]
            else:
                res+=d[S[i]]
        return res
t=int(input())
for i in range(len(t):
    ob=solution()
    S=input()
    print(ob.romanToDecimal(S))
