#include<bits/stdc++.h>
// #include<atcoder/all>
// using namespace atcoder;
using namespace std;
struct Init { Init() { ios::sync_with_stdio(0); cin.tie(0); cout << setprecision(13); } }init;
using ll = long long;
using pll = pair<ll, ll>;
using Field = vector<string>;
template<typename T> using Board = vector<vector<T>>;
using Graph = vector<vector<int>>;
template<typename T> using min_pq = priority_queue<T, vector<T>, greater<T>>;
const int inf = 1073741823;
const long long INF = 1LL << 60;
const int MOD1 = 1000000007; // 計算するたびにこまめに %MOD する.
const int MOD9 = 998244353; // ↑最後にも %MOD をする
const int SIGMA = 26;
#define el '\n'
#define spa " "
#define pb emplace_back
#define rep(i, s, n) for(int i = (s); i < (int)(n); i++)
#define rrep(i, s, n) for(int i = (int)(n) - 1; i >= (s); i--)
#define Yes cout << "Yes" << el
#define No cout << "No" << el
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define unless(c) if(!(c))
#define until(c) while(!(c))
#define idx(i, j) ((i) * w + (j)) // 横幅の変数名は w であることが前提.
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }

int sub(){
    return 0;
}

int solve(){

    return 0;
}

int main(){
    int t = 1;
    // cin >> t;
    rep(i, 0, t){
        solve();
    }
    return 0;
}
