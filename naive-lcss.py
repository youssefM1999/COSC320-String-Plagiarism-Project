from time import time
import sys

sys.setrecursionlimit(15000)

src_file = open("Dataset/plagiarism_source.txt", encoding="utf-8")
sus_file = open("Dataset/plagiarism_sus.txt", encoding="utf-8")

src = src_file.read()
sus = sus_file.read()

src = src.lower()
sus = sus.lower()

src_processed = ' '.join(src.split('\n'))
src_length = len(src_processed)
sus_processed = ' '.join(sus.split('\n'))
sus_length = len(sus_processed)

# print(sus_processed)

def lcss_naive(src, sus, m, n):
    
    score = 0

    for i in range(m):
        for j in range(n):
            k = 0
            while(i + k < m and j + k < n and src[i+k] == sus[j+k]):
                k += 1
            if(k > score):
                score = k
    return score

   #  if m == 0 or n == 0:
   #     return 0
   #  elif src[m-1] == sus[n-1]:
   #     return 1 + lcss(src, sus, m-1, n-1)
   #  else:
   #     return max(lcss(src, sus, m, n-1), lcss(src, sus, m-1, n))
    
t0 = time()
longest_subsequence = lcss_naive(src_processed, sus_processed, src_length, sus_length)
t1 = time()

# print(longest_subsequence)
print(t1-t0)
