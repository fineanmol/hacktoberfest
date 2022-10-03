// LANGUAGE: C++
// AUTHOR: Himanshu Gupta
// GITHUB: https://github.com/himanshugupta11110000
class Solution {
public:

	bool canBeNext(string s1, string s2){
		int uncmn=0;
		for(int i=0; i<s1.size(); i++)
			uncmn += (s1[i] != s2[i]);

		return uncmn==1;
	}

	void bfs(vector<vector<int>>& graph, vector<int> parent[], int n, int start, int end){
		vector<int> dist(n, 501);

		queue<int> q; 
		q.push(start);

		dist[start] = 0; 
		parent[start] = {-1};

		while(!q.empty()){
			int curr = q.front();
			q.pop();

			for( int node: graph[curr]){
				if(dist[node] > dist[curr]+1){ 
					dist[node] = dist[curr]+1;
					q.push(node);
					parent[node].clear();
					parent[node].push_back(curr); 
				}else if(dist[node] == dist[curr]+1) 
					parent[node].push_back(curr);
			}
		}

	}

	void shortestPaths(int node, vector<vector<int>>& Paths, vector<int>& curr_path, vector<int> parent[]){
		if(node == -1){ 
			Paths.push_back(curr_path);
			return;
		}

		for(int p: parent[node]){ 
			curr_path.push_back(p);
			shortestPaths(p, Paths, curr_path, parent);
			curr_path.pop_back();
		}
	}

	vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
		int start=-1, end=-1;

		for(int i=0; i<wordList.size(); i++){
			if(wordList[i] == beginWord)
				start = i;
			if(wordList[i] == endWord)
				end = i;
		}

		if(end == -1)
			return {};

		if(start == -1){
			wordList.emplace(wordList.begin(), beginWord);
			start = 0;
			end++;
		}

		int n = wordList.size();
		vector<vector<int>> graph(n, vector<int>());

		for(int i=0; i<n; i++){
			for(int j=i+1; j<n; j++){
				if(canBeNext(wordList[i], wordList[j])){
					graph[i].push_back(j);
					graph[j].push_back(i);
				}
			}
		}

		vector<int> parent[n];
		bfs(graph, parent, n, start, end);

		vector<vector<int>> Paths;
		vector<int> curr_path;
		shortestPaths(end, Paths, curr_path, parent);

		vector<vector<string>> ans;

		for(auto path: Paths){
			vector<string> curr;

			for(int i=0; i<path.size()-1; i++)
				curr.push_back(wordList[path[i]]);

			reverse(curr.begin(), curr.end());  
			curr.push_back(wordList[end]);
			ans.push_back(curr);
		}

		return ans;
	}
};
