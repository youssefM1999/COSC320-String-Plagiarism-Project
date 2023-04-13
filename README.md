# COSC 320 - Algorithm Analysis Project

### Team and Contributions

Esteban Martinez (22717805)

-   `main.py` and `kmp.py`
-   `README.md`

Youssef Mahmoud (37624970)

-   `naive_lcss`
-   `dynamic_lcss`

Khalid Mahmoud (28842458)

-   `rabin_karp.py`

## Project Structure

This project focused on analysing the performance of three algorithms for string matching in the conext of detecting plagiarism:

-   Rabin-Karp
-   Knuth-Morris-Pratt (referred to as KMP)
-   Longest Common Substring (LCSS)

The project is broken down into three directories and one `main.py` file which is the entry point for the program.

-   `Algorithms` includes the four algorithms which are ran for analysis in their respective files. These are all wrapped in functions which are called in `main.py`.
-   `Data` includes two directories, `external-detection-corpus` and `test-corpus`.
    -   `external-detection-corpus` is a corpus of 500 source documents and 500 potentially plagiarised documents which compose the main testing set. (**add source**)
    -   `test-corpus` is a corpus of 11 source and 11 suspicious documents. The 11 source documents were pulled from a variety of news and scholarly articles, and the suspicious documents were synthetically plagiarised using OpenAI's ChatGPT, as well as manual input.
-   `Plots` includes all the output plots from `main.py`

## How it Works

`main.py` is a simple program for running the algorithms, and can be easily edited to run on different files by editing the `src_dataset` and `sus_dataset` file paths. The program defines the `testAlgorithm` function, and calls it to run the algorithms on the dataset.

## Problems Encountered

Due to the massive size of some of the files, the program can take an enormous amount of time to compute. For this reason, we decided to use a compute dedicated cloud computer using the Google Cloud Compute Engine API (AMD based, 8 core, 32 GB RAM) to do our large calculations.

This allowed us to produce graphs for the KMP and Rabin Karp algorithms with our large dataset, but we still ran into memory issues with our LCSS algorithms. This was because our LCSS implementations used a 2D array, as well as temporary storage for our files in the form of `src_processed` and `sus_processed`.

For this reason, we created another implementation, `optimized_lcss.py` which instead iterates the files line by line to check for longest common subsequences and does not created a processed version of the file. It also does not create a 2D array and instead uses 2 different arrays.

With this new file we were able to produce a graph using our large dataset.

## How to Run

1. Clone the repository
2. Use the command `pip install -r requirements.txt` to install the required packages
3. Run `import nltk` in a python shell and run `nltk.download("punkt")` to download the required nltk package for the KMP implementation
4. Run `python main.py` to run the program

## Results

### Large Dataset

Rabin Karp Algorithm with Large Dataset
![Rabin Karp Algorithm with Large Dataset](<./Plots/Rabin%20Karp%20(BIG).png>)

KMP Algorithm with Large Dataset
![KMP Algorithm with Large Dataset](<./Plots/KMP%20(BIG).png>)

Optimized LCSS Algorithm with Large Dataset
![Optimized LCSS Algorithm with Large Dataset](<./Plots/Optimized%20LCSS%20(BIG).png>)

### Small Dataset

Rabin Karp Algorithm with Small Dataset
![Rabin Karp Algorithm with Small Dataset](./Plots/Rabin%20Karp.png)

KMP Algorithm with Small Dataset
![KMP Algorithm with Small Dataset](./Plots/KMP.png)

Optimized LCSS Algorithm with Small Dataset
![Optimized LCSS Algorithm with Small Dataset](./Plots/Optimized%20LCSS.png)

Dynamic LCSS Algorithm with Small Dataset
![Dynamic LCSS Algorithm with Small Dataset](./Plots/Dynamic%20LCSS.png)

Naive LCSS Algorithm with Small Dataset
![Naive LCSS Algorithm with Small Dataset](./Plots/Naive%20LCSS.png)
