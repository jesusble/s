def lcs(X, Y, m, n): 
    L = [[0 for i in range(n + 1)]  
            for i in range(m + 1)]  
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1
            else: 
                L[i][j] = max(L[i - 1][j],  
                              L[i][j - 1])
    return L[m][n]
def findMinCost(X, Y, costX, costY): 
  
    m = len(X) 
    n = len(Y) 
    len_LCS =lcs(X, Y, m, n) 
    return (costX * (m - len_LCS) +
            costY * (n - len_LCS)) 
X = "ef"
Y ="gh"
print(end = '') 
print( findMinCost(X, Y, 10, 20)) 
  
