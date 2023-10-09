class comparator{
        public:
          bool operator()(const pair<int,int>& p1,const pair<int,int>& p2){
              if(p2.second < p1.second){
                  return true;
              }
              else{
                  return false;
              }
          }  
    };
    
    vector <int> dijkstra(int V, vector<vector<int>> adj[], int S)
    {
        // Code here
        vector<int> dis(V,INT_MAX);
        //priority_queue to take min path everytime starting
        //pair of node,dis
        priority_queue<pair<int,int>,vector<pair<int,int>>,comparator> pq;
        
        //dis from src to src =0
        
        //it contains minimum distance from sorce t vertex i
        dis[S] = 0;
        pq.push({S,0});
        
        while(!pq.empty()){
            pair<int,int> frontN = pq.top();
            int srcNode = frontN.first;
            int srcDis = frontN.second;
            pq.pop();
            
            for(auto i: adj[srcNode]){
                //i is {node,dis} in adj list
                int adjNode = i[0];
                int adjDis = i[1];
                int newDis = srcDis + adjDis; 
                if(newDis < dis[adjNode]){
                    dis[adjNode] = newDis;
                    pq.push({adjNode,newDis});
                }
            }
        }
        
        
        
        return dis;
    }
