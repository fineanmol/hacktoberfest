#include <bits/stdc++.h>
using namespace std;
#define fastIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define lli long long
#define pii pair<lli, lli>
#define fi first
#define sc second
#define pb push_back
#define ppb pop_back
#define EB emplace_back
#define MP make_pair
#define vi vector<lli>
#define vpii vector<pii>
#define vov vector<vi>
#define vovp vector<vector<pii>>
#define mp map<lli, lli>
#define inp(v) for (auto& x : v) cin >> x;
#define all(v) (v).begin(), (v).end()

// Loops
#define rep(i, a, b) for (lli i = a; i*i <= b; i++)
#define fr(i, n) for (lli i = 0; i < n; ++i)
#define br(n, i) for (lli i = n; i >= 0; --i)
#define per(i, b, a) for (lli i = b; i >= a; --i)
#define vovfr(i, n, j, m) fr(i, n) fr(j, m)

// Input helpers
#define readGraph(adj, m) fr(i, m) { lli u, v; cin >> u >> v; adj[u].pb(v); adj[v].pb(u); }
#define readGraphDir(adj, m) fr(i, m) { lli u, v; cin >> u >> v; adj[u].pb(v); }

// Graph/DSU/Tree Helpers
#define adjlist(n) vector<vi> adj(n)
#define vis(n) vector<bool> vis(n, false)
#define parent(n) vi par(n, -1)
#define dsu_find(x) (par[x] < 0 ? x : par[x] = dsu_find(par[x]))
#define dsu_union(x, y) if ((x = dsu_find(x)) != (y = dsu_find(y))) { par[y] += par[x]; par[x] = y; }
#define edge(u, v) adj[u].pb(v); adj[v].pb(u);

// Priority Queue Shortcuts
#define minpq priority_queue<lli, vi, greater<lli>>
#define maxpq priority_queue<lli>

// Debugging
#define dbg(x) cerr << #x << " = " << x << "\n";
#define dbg2(x, y) cerr << #x << " = " << x << ", " << #y << " = " << y << "\n";
#define printVec(v) for (auto x : v) cout << x << " "; cout << "\n";

// Constants
const lli INF = 1e18;
const lli MOD = 1e9 + 7;

#define yes cout << "YES\n"
#define no cout << "NO\n"

lli gcd(lli a, lli b){return b == 0 ? a : gcd(b,a%b);}
lli binpow(lli base, lli expo){
    if(expo == 0)return 1;

    if(expo%2 == 1){
        return (base * binpow(base , expo-1));
    }else{
        lli temp = binpow(base , expo / 2);
        return (temp * temp);
    }
}

/*
	Small Observation     
      
      
*/


/*
	Claims on Algo      
      
      
*/
bool isPrime(lli n){
    rep(i,2,n){
        if(n%i == 0)return 0;
    }
    return 1;
}
void solve(){
    lli n;cin >> n;
    
    if((n&1)^1)cout << n/2 << " " << n/2 << "\n";
    else{
        if(isPrime(n)){
            cout << 1 << " " << n-1 << "\n";
        }else{
            // lli mini = LLONG_MAX;
            // for(lli i = 1;i<n/2;++i){
            //     mini = min(mini,((i*(n-i)/gcd(i,n-i))));
            // }
            // cout << n-mini << " " << mini << "\n";
            lli fac = 1;
            for(lli i = 2;i*i<=n;++i){
                if(n%i == 0){
                    cout << n/i << " " << n-(n/i) << "\n";
                    break;
                }
            }
        }
    }
}
signed main(){
    fastIO;
    lli t=1;
    cin >> t;
    while(t--){
        solve();
    }
}
