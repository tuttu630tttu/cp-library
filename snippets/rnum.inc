ll rnum(ll n){
  if(n == 0) return 0;
  ll res = 0;
  while (n > 0){
    res = res*10 + (n%10);
    n /= 10;
  }
  return res;
}
