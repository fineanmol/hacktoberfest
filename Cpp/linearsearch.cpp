#include <iostream>
#include <vector>
#include <iterator>

template <typename ForwardIt, typename T>
ForwardIt linear_search(ForwardIt first, ForwardIt last, const T& value) {
   for (; first != last; ++first) {
      if (*first == value) return first;
   }
   return last;
}

int main() {
   std::ios::sync_with_stdio(false);
   std::cin.tie(nullptr);

   size_t n;
   if (!(std::cin >> n)) return 0;

   std::vector<long long> a(n);
   for (size_t i = 0; i < n; ++i) std::cin >> a[i];

   long long target;
   std::cin >> target;

   auto it = linear_search(a.begin(), a.end(), target);
   if (it == a.end()) {
      std::cout << -1 << '\n';
   } else {
      std::cout << std::distance(a.begin(), it) << '\n';
   }
   return 0;
}