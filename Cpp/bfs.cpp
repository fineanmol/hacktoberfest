#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct BFSResult {
   vector<int> order;   // visitation order
   vector<int> dist;    // distance from source (edges), -1 if unreachable
   vector<int> parent;  // parent in BFS tree, -1 for source/unreached
};

BFSResult bfs(const vector<vector<int>>& adj, int s) {
   int n = (int)adj.size();
   vector<int> dist(n, -1), parent(n, -1), order;
   queue<int> q;

   dist[s] = 0;
   q.push(s);

   while (!q.empty()) {
      int u = q.front(); q.pop();
      order.push_back(u);

      for (int v : adj[u]) {
         if (dist[v] != -1) continue; // already visited
         dist[v] = dist[u] + 1;
         parent[v] = u;
         q.push(v);
      }
   }
   return {order, dist, parent};
}

vector<int> reconstruct_path(int target, const vector<int>& parent) {
   vector<int> path;
   for (int v = target; v != -1; v = parent[v]) path.push_back(v);
   reverse(path.begin(), path.end());
   // if parent[path.front()] != -1 then target wasn't connected to the source used for BFS
   return path;
}

int main() {
   ios::sync_with_stdio(false);
   cin.tie(nullptr);

   // Input format:
   // n m
   // m lines: u v  (0-indexed vertices)
   // s          (source vertex)
   // Graph is treated as undirected. For directed, comment out the second push_back.
   int n, m;
   if (!(cin >> n >> m)) return 0;

   vector<vector<int>> adj(n);
   for (int i = 0; i < m; ++i) {
      int u, v;
      cin >> u >> v;
      adj[u].push_back(v);
      adj[v].push_back(u); // remove this line for directed graphs
   }

   int s;
   cin >> s;

   BFSResult res = bfs(adj, s);

   cout << "BFS order:";
   for (int v : res.order) cout << ' ' << v;
   cout << '\n';

   cout << "Distances:\n";
   for (int i = 0; i < n; ++i) {
      cout << i << ": " << res.dist[i] << '\n';
   }

   cout << "Parents:\n";
   for (int i = 0; i < n; ++i) {
      cout << i << ": " << res.parent[i] << '\n';
   }

   // Example: reconstruct path from s to some target t if reachable
   // Uncomment to test with a specific target t
   // int t = 0;
   // if (res.dist[t] != -1) {
   //     auto path = reconstruct_path(t, res.parent);
   //     cout << "Path " << s << " -> " << t << ":";
   //     for (int v : path) cout << ' ' << v;
   //     cout << '\n';
   // } else {
   //     cout << "No path from " << s << " to " << t << '\n';
   // }

   return 0;
}