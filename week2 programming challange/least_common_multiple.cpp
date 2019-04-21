#include <iostream>
int gcd_naive(int a, int b) {
   if (a == 0) 
       return b; 
    if (b == 0) 
       return a; 
    if (a == b) 
        return a; 
    if (a > b) 
        return gcd_naive(a%b, b); 
    return gcd_naive(a, b%a); 
}
long long lcm_naive(int a, int b) {
  return (long long) a * b/gcd_naive(a,b);
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_naive(a, b) << std::endl;
  return 0;
}
