#include <bits/stdc++.h>
using namespace std;
#define int long long
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define vi vector<int>
#define vvi vector< vector<int> >
#define pi pair<int,int>
#define vii vector<pi>
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
const int M=1e9+7;

void solve() {
    int m,n,p;
    cin>>m>>n>>p;
    vvi v(m, vi(n,0));
    vi ma(n,0);
    rep(i,0,m) rep(j,0,n) cin>>v[i][j];
    rep(i,0,n) {
        rep(j,0,m) {
            ma[i]=max(v[j][i], ma[i]);
        }
    }
    int ans=0;
    rep(i,0,n) {
        ans+=ma[i]-v[p-1][i];
    }
    cout<<ans<<'\n';
}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int T=1;
    cin>>T;
    rep(TestCase, 1, T+1) {
        cout<<"Case #"<<TestCase<<": ";
        solve();
    }
    return 0;
}
