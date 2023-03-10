def lcss(src, sus):
    # find the length of the strings
    m = len(src)
    n = len(sus)
 
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
 
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of src[0..i-1]
    and sus[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif src[i-1] == sus[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = masrc(L[i-1][j], L[i][j-1])
 
    # L[m][n] contains the length of LCS of src[0..n-1] & sus[0..m-1]
    return L[m][n]