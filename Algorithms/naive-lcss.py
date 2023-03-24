from time import time
import sys

sys.setrecursionlimit(15000)

src_file = open("Dataset/plagiarism_source_test.txt", encoding="utf-8")
sus_file = open("Dataset/plagiarism_sus_test.txt", encoding="utf-8")

src = src_file.read()
sus = sus_file.read()

src = src.lower()
sus = sus.lower()

src_processed = ' '.join(src.split('\n'))
src_length = len(src_processed)
sus_processed = ' '.join(sus.split('\n'))
sus_length = len(sus_processed)


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

    
t0 = time()
longest_subsequence = lcss_naive(src_processed, sus_processed, src_length, sus_length)
t1 = time()

# print(longest_subsequence)
print("The longest common subsequence in this text is: " + str(longest_subsequence))
print("The running time of this algorithm is: " + str(t1-t0))
