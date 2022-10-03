#include<bits/stdc++.h>
using namespace std;

vector<int>toposort(int n,vector<int>adj[]){
queue<int>q;
vector<int>indegree(n,0);
for(int i=0;i<n;i++){
    for(auto it:adj[i]){
        indegree[it]++;
    }
}
for(int i=0;i<n;i++){
    if(indegree[i]==0){
        q.push(i);
    }
}
vector<int>topo;
while(!q.empty()){
    int x=q.front();
    q.pop();
    topo.push_back(x);
    for(auto it:adj[x]){
        indegree[it]--;
        if(indegree[it]==0){
            q.push(it);
        }
    }
}
return topo;
}

int main(){
    int n,m;
    cin>>n>>m;
    vector<int>adj[n];
    for(int i=0;i<m;i++){
        int x,y;
        cin>>x>>y;
        adj[x].push_back(y);
    }
    vector<int>topo=toposort(n,adj);
    cout<<"topological sort of given graph is as follows\n";
    for(int i=0;i<n;i++){
        cout<<topo[i]<<" ";
    }
    return 0;
}
