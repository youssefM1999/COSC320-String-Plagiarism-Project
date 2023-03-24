from time import time
import sys

sys.setrecursionlimit(15000)

src_file = open("Dataset/plagiarism_source_5.txt", encoding="utf-8")
sus_file = open("Dataset/plagiarism_sus_5.txt", encoding="utf-8")

src = src_file.read()
sus = sus_file.read()

src = src.lower()
sus = sus.lower()

src_processed = ' '.join(src.split('\n'))
src_length = len(src_processed)
sus_processed = ' '.join(sus.split('\n'))
sus_length = len(sus_processed)


def lcss_dynamic(src, sus):
    # find the length of the strings
    m = len(src)
    n = len(sus)

    print(m)
    print(n)

    lcss = [[0] * (n+1) for _ in range(m+1)]
    result = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if src[i-1] == sus[j-1]:
                lcss[i][j] = lcss[i-1][j-1] + 1
                result = max(result, lcss[i][j])
            else:
                lcss[i][j] = 0
    return result

t0 = time()
longest_subsequence = lcss_dynamic(src_processed, sus_processed)
t1 = time()

print("The longest common subsequence in this text is: " + str(longest_subsequence))
print("The running time of this algorithm is: " + str(t1-t0))