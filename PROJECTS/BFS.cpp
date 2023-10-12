#include <bits/stdc++.h>
#include <queue>
using namespace std;

// BFS is a way of traversing a graph
// Here we, use same concept as we used in level order traversal of tree
// But, since vertex can be repeated here unlike trees, we need to maintain a state for
// each vertex to know whether it has been visited or not

void addAdj(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

// 0 - 1 - 3   4 -5
//  '2'         '6

void BFS(vector<int> adj[], int s, vector<bool> &isVisited)
{
    queue<int> q;
    q.push(s);
    isVisited[s] = true;
    while (!q.empty())
    {
        for (int x : adj[q.front()])
        {
            if (!isVisited[x])
            {
                q.push(x);
                isVisited[x] = true;
            }
        }
        cout << q.front() << "  ";
        q.pop();
    }
}
// 0 1 2 3 4 5 6

void genBFS(vector<int> adj[], int V)
{
    int count = 0;
    vector<bool> isVisited(V, false);
    for (int i = 0; i < V; i++)
    {
        if (!isVisited[i])
        {
            count++;
            BFS(adj, i, isVisited);
        }
    }
    cout << endl
         << "Total components: " << count << endl;
}
// Time complexity = O(V+E)

int main()
{
    int V = 7;
    vector<int> adj[V];
    addAdj(adj, 0, 1);
    addAdj(adj, 0, 2);
    addAdj(adj, 1, 2);
    addAdj(adj, 1, 3);
    addAdj(adj, 4, 5);
    addAdj(adj, 4, 6);
    genBFS(adj, V);

    return 0;
}
