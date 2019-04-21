#include <iostream> 
using namespace std; 
int countRefill(int N, int K, int M, int compulsory[]) 
{ 
	int count = 0; 
	int i = 0; 
	int distCovered = 0; 
	while (distCovered < N) { 
		if (i < M && compulsory[i] <= (distCovered + K)) { 
            distCovered = compulsory[i];
			i++; 
		}
		else
			distCovered += K;
		if (distCovered>N)
		return -1;
		if (distCovered < N) 
			count++; 
	} 

	return count; 
} 
int main() 
{ 
	int N = 0;
	cin>>N; 
	int K = 0;
	cin>>K; 
	int M = 0;
	cin>>M;
	int c[M];
	for(int i=0;i<M;i++)
	cin>>c[i];
	cout << countRefill(N, K, M, c) << endl; 
	return 0; 
} 
