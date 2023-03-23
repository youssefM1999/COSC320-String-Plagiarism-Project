def KMP(pat, text):
    # *KMP search implementation
    N = len(text)
    M = len(pat)
    lps = [0] * M  # longest prefix that is also a suffix
    computeLPS(lps, pat, M)

    j = 0
    for i in range(0, N):
        if text[i] == pat[j+1]:


def computeLPS(lps, pat, M):
    # *longest proper prefix preprocessing

    len_lps = 0  # length of the longest prefix suffix value
    lps[0] = 0
    i = 1

    while i < M:
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1
        elif len_lps != 0:
            len_lps = lps[len_lps-1]
        else:
            lps[i] = 0
            i += 1

# *main


text = "AAAABAAAAAABAACAABAA"
pat = "AABAACAABAA"
