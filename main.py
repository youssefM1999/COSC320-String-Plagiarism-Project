from time import time
from Algorithms import kmp

t0 = time()
kmp.runKMP("Dataset\plagiarism_source_10.txt",
           "Dataset\plagiarism_sus_10.txt")
t1 = time()

print(f"Ran KMP in {t1-t0} seconds")
