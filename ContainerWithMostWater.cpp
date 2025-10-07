#include <bits/stdc++.h>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int maxWater = 0;
    
    while (left < right) {
        int currentHeight = min(height[left], height[right]);
        int currentWidth = right - left;
        int currentArea = currentHeight * currentWidth;
        maxWater = max(maxWater, currentArea);
        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxWater;
  }
int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    
    cout << maxArea(height) << endl;
    return 0;
  }
