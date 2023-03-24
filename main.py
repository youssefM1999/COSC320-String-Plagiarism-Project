from time import time
from Algorithms import kmp

t0 = time()
kmp.runKMP("Test\source.txt",
           "Test\sus.txt")
t1 = time()

print(f"Ran KMP in {t1-t0} seconds")
