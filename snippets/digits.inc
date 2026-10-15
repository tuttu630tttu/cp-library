vector<int> digits(ll n){
  if(n == 0) return {0};
  vector<int> res;
  while (n > 0){
    res.pb(n%10);
    n /= 10;
  }
  reverse(all(res));
  return res;
}
