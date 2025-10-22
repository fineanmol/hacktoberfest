/*
 * Problem: Stock Span Problem
 * Language: C++
 * Author: [Bhavika Wankhede]
 * Hacktoberfest Contribution 2025
 *
 * Description:
 * This program solves the Stock Span Problem using a stack to achieve O(n)
 * time complexity. Given daily prices of a stock, it calculates for each day
 * the maximum number of consecutive previous days (including today) where the
 * stock price was less than or equal to the current day's price.
 *
 * The algorithm efficiently tracks previous stock prices using a stack of indices,
 * allowing span calculation without nested loops.
 *
 * Operations:
 *  - Input: An array of stock prices for n consecutive days.
 *  - Output: An array of spans, where each span[i] represents the stock span 
 *            for day i.
 *
 * Algorithmic Complexity:
 *  - Time:  O(n)  // Each element is pushed and popped from the stack at most once
 *  - Space: O(n)  // Stack stores indices of elements
 */


class StockSpanner{
public:
  stack<pait<int,int>>st;
  vector<int>ans;
  StockSpanner(){
    index=-1;
  }
  int next(int value){
    index=index+1;
    while(!st.empty() && st.top().first<=value){
        st.pop();
    }
    ans=index-(st.empty()?-1 : st.top().second);

    st.push({value, index});
    return ans
 }
};