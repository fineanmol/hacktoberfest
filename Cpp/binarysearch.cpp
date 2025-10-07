#include <bits/stdc++.h>
using namespace std;

// Returns the first index of key in sorted array a, or -1 if not found.
int binary_search_first(const vector<long long>& a, long long key) {
   int left = 0, right = static_cast<int>(a.size()); // [left, right)
   while (left < right) {
      int mid = left + (right - left) / 2;
      if (a[mid] < key) left = mid + 1;
      else right = mid;
   }
   if (left < static_cast<int>(a.size()) && a[left] == key) return left;
   return -1;
}

int main() {
   ios::sync_with_stdio(false);
   cin.tie(nullptr);

   int n;
   if (!(cin >> n)) return 0;

   vector<long long> a(n);
   for (int i = 0; i < n; ++i) cin >> a[i];

   // Input must be sorted in non-decreasing order.
   // Uncomment to enforce sorting (optional):
   // sort(a.begin(), a.end());

   long long key;
   while (cin >> key) {
      cout << binary_search_first(a, key) << '\n';
   }

   return 0;
}