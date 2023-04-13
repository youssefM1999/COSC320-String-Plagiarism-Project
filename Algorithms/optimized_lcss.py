from time import time

# This code is a memory optimized version of the dynamic programming
# The main optimizations are in running the algorithm line by line instead of file by file, not using src_processed and sus_processed, and not using the 2D array (instead using prev and curr arrays)


def runLCSS_optimized(src_file_str: str, sus_file_str: str):
    src_file = open(src_file_str, encoding="utf-8")
    sus_file = open(sus_file_str, encoding="utf-8")

    longest_subsequence = 0
    t0 = time()

    for src_line, sus_line in zip(src_file, sus_file):
        src_line = src_line.lower().rstrip()
        sus_line = sus_line.lower().rstrip()

        m = len(src_line)
        n = len(sus_line)

        prev = [0] * (n+1)
        curr = [0] * (n+1)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if src_line[i-1] == sus_line[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
            curr[0] = 0

        longest_subsequence += prev[n]

    t1 = time()

    print("The longest common subsequence in this text is: " +
          str(longest_subsequence))
    # print("The running time of this algorithm is: " + str(t1-t0))

    src_file.close()
    sus_file.close()
