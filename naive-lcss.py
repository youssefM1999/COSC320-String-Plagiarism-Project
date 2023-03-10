def lcs(src, sus, m, n):
 
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(src, sus, m-1, n-1)
    else:
       return max(lcs(src, sus, m, n-1), lcs(src, sus, m-1, n))
 