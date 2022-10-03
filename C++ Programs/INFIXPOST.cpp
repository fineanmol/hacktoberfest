#include<iostream>
#include<string>
#include<stack>
using namespace std;

int precedence(char c){
    if(c=='^'){
        return 3;
    }
    else if(c=='*'||c=='/'){
        return 2;
    }
    else if(c=='+'||c=='-'){
        return 1;
    }
    else{
        return 0;
    }
}

int isOperator(char c){
    if(c=='^'||c=='*'||c=='/'||c=='+'||c=='-'||c==')'||c=='('){
        return 1;
    }
    else{
        return 0;
    }
}

int rtol(char c){
    if(c=='^'){
        return 1;
    }
    else{
        return 0;
    }
}

string infixtopostfix(string s){
    stack<char>st;
    string res;
    for(int i=0;i<s.length();i++){
       
      
        if(!isOperator(s[i])){
            res+=s[i];
            
         }
         else if(s[i]=='('){
            st.push(s[i]);
         }
         else if(s[i]==')'){
            while(!st.empty()&&st.top()!='('){
                res+=st.top();
                st.pop();
            }  
            if(!st.empty()){
                st.pop();
            }

         }
         else{
            
                while(!st.empty()&&(precedence(st.top())>=precedence(s[i]))){
                    if (s[i]=='^'&&st.top()!='^')
                    {
                        break;
                    }
                    else{
                        res+=st.top();
                        st.pop();
                    }
                }
                st.push(s[i]);

                    
                

            }
           


            }
            // while(!st.empty()&&(precedence(st.top())>precedence(s[i]))){
            //     res+=st.top();
            //     st.pop();
            // }
            // st.push(s[i]);



    while(!st.empty())
    {
        res +=st.top();
        st.pop();
    }

    return res;
    
}



int main(){
    string res;
    cout<<"Enter the infix expression";
    cin>>res;
    cout<<infixtopostfix(res);
}
