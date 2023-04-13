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

`main.py` is a simple program for running the algorithms, and can be easily edited to run on different files by editing the `src_dataset` and `sus_dataset` file paths. The program defines the `testAlgorithm` function, and calls it to run the algorithms on the dataset. It is currently configured to run on the last 10 files of the dataset.

Due to the massive size of some of the files, the program can take an enormous amount of time to compute.

## How to Run

TODO: ADD nltk.download("punkt") to instructions
