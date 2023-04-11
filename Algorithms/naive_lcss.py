from time import time
import sys

sys.setrecursionlimit(15000)


def runLCSS_naive(src_file_str: str, sus_file_str: str):
    src_file = open(src_file_str, encoding="utf-8")
    sus_file = open(sus_file_str, encoding="utf-8")

    src = src_file.read()
    sus = sus_file.read()

    src = src.lower()
    sus = sus.lower()

    src_processed = ' '.join(src.split('\n'))
    src_length = len(src_processed)
    sus_processed = ' '.join(sus.split('\n'))
    sus_length = len(sus_processed)

    def lcss_naive(src, sus):

        m = len(src)
        n = len(sus)

        score = 0

        for i in range(m):
            for j in range(n):
                k = 0
                while (i + k < m and j + k < n and src[i+k] == sus[j+k]):
                    k += 1
                if (k > score):
                    score = k
        return score

    t0 = time()
    longest_subsequence = lcss_naive(src_processed, sus_processed)
    t1 = time()

    # print(longest_subsequence)
    print("The longest common subsequence in this text is: " +
          str(longest_subsequence))
    # print("The running time of this algorithm is: " + str(t1-t0))
