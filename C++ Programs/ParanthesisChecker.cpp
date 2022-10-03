class stack1
{
  public:
    char *arr;
    char topChar;
    int top;
    stack1()
    {
        
    }
    stack1(int n)
    {
        top = -1;
        arr = new char[n];
    }
    void push(char ele)
    {
        top++;
        arr[top] = ele;
    }
    char pop()
    {
        if(top == -1)
            return '0';
        else
        {
            topChar = arr[top];
            top--;
            return topChar;
        }
    }
    char peek()
    {
        return arr[top];
    }
};
class Solution
{
    public:
    //Function to check if brackets are balanced or not.
    bool ispar(string x)
    {
       
        int i,len = x.size();
        char expLet;
        stack1 obj(len);
        for(i=0;i<len;i++)
        {
            if(x[i] == '{' || x[i] == '(' || x[i] == '[')
                obj.push(x[i]);
            else if(x[i] == '}')
            {
                if(obj.pop() != '{')
                    return false;
               
            }
            else if(x[i] == ')')
            {
                if(obj.pop() != '(')
                    return false;

            }
            else if(x[i] == ']')
            {
                if(obj.pop() != '[')
                    return false;
            }

        }

        if(obj.pop() == '0')
            return true;
        else
            return false;
    }

};
