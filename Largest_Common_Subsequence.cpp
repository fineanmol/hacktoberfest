#include<bits/stdc++.h>
#include<vector>
using namespace std;

int main()
{
    string s2="AGCCCTAAGGGCTACCTAGCTT";
    string s1="GACAGCCTACAAGCGTTAGCTTG";

    int n=s1.length();
    int m=s2.length();
    vector<vector<pair<int,char>>>v(n+1,vector<pair<int,char>>(m+1));

    for(int i=0; i<=n; i++)
        v[i][0]={0,'N'};
    for(int i=0; i<=m; i++)
        v[0][i]={0,'N'};
    
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=m; j++)
        {
            if(s1[i-1]==s2[j-1])
            {
                v[i][j]={v[i-1][j-1].first+1,'D'};
            }else
            {
                if(v[i-1][j].first>v[i][j-1].first)
                {
                	v[i][j]={v[i-1][j].first,'T'};
				}
                else
                    v[i][j]={v[i][j-1].first,'L'};
            }
        }
    }
    for(int i=0; i<=n; i++)
    {
        for(int j=0; j<=m; j++)
        {
            cout<<"{"<<v[i][j].first<<","<<v[i][j].second<<"} ";
        }
        cout<<endl;
    }
    bool flag=true;
    pair<int,char>itr=v[n][m] ;

    int n_t=n, m_t=m;
    string str="";
    while(n_t!=0 && m_t!=0 && itr.second!='N')
    {
        if(itr.second=='D')
        {
            cout<<s2[m_t-1];
            str+=s2[m_t-1];
            n_t--,m_t--;
            itr=v[n_t][m_t];
            
        }
        else if(itr.second=='L')
        {
            m_t--;
            itr=v[n_t][m_t];    
        }
        else if( itr.second=='T')
        {
            n_t--;
            itr=v[n_t][m_t];
        }
        else
        {
            break;
        }
    }
    
    cout<<"\nlongest Substring Sequence is : ";
    for (int i = str.length() - 1; i >= 0; i--)
        cout << str[i];

    cout<<endl;

}