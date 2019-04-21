#Uses python3
import sys 
def minCoins(coins, m, V): 
	table = [0 for i in range(V + 1)] 
	table[0] = 0
	for i in range(1, V + 1): 
		table[i] = sys.maxsize 
	for i in range(1, V + 1): 
		for j in range(m): 
			if (coins[j] <= i): 
				sub_res = table[i - coins[j]] 
				if (sub_res != sys.maxsize and
					sub_res + 1 < table[i]): 
					table[i] = sub_res + 1
	return table[V] 
if __name__ == "__main__": 

	coins = [1,3,4] 
	m = len(coins) 
	V =int(input())
	print(minCoins(coins, m, V)) 
