import glob
from natsort import natsorted, ns
from time import time
from Algorithms import kmp, dynamic_lcss, naive_lcss

kmp_times = []
naive_lcss_times = []
dynamic_lcss_times = []

src_dataset = natsorted(glob.glob("Dataset/Source/*.txt"), alg=ns.IGNORECASE)

sus_dataset = natsorted(
    glob.glob("Dataset/Suspicious/*.txt"), alg=ns.IGNORECASE)

print("Source files: " + str(src_dataset))
print("Suspicious files: " + str(sus_dataset))


for i in range(src_dataset.__len__()):
    src_file = src_dataset[i]
    sus_file = sus_dataset[i]

    # KMP run (linear time)
    t0 = time()
    kmp.runKMP(src_file,
               sus_file)
    t1 = time()
    kmp_times.append(t1-t0)

    # LCSS naive run (quadratic time)
    # t0 = time()
    # naive_lcss.runLCSS_naive(
    #     src_file, sus_file)

    # t1 = time()
    # naive_lcss_times.append(t1-t0)

    # LCSS dynamic run (quadratic time)
    # t0 = time()
    # dynamic_lcss.runLCSS_dynamic(
    #     src_file, sus_file)

    # t1 = time()
    # dynamic_lcss_times.append(t1-t0)

print("KMP running times: " + str(kmp_times))
# print("Naive LCSS running times: " + str(naive_lcss_times))
# print("Dynamic LCSS running times: " + str(dynamic_lcss_times))
