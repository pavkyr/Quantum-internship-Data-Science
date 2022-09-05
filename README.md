# Quantum internship Data Science
 Test Task

---

## Code and Resources Used

**Python Version:** 3.10.6

**Packages:** pandas, numpy, seaborn, sklearn, matplotlib, time, cv2, shapely, geopandas, rasterio, numba, gmpy2

---

### Task 1 - What is FOR loop?
You have a positive integer number N as an input. Please write a program in Python 3 that calculates the sum in range 1 and N.

Limitations:
N <= 10^25;
Execution time: 0.1 seconds

**Solution ideas:**
Since Python is considered a slow programming language, I used the Numba library (open source JIT compiler that translates a subset of Python and NumPy code into fast machine code) to speed up the calculations. as a result, when n is less than 10^9, the calculations take ~0.001s, in contrast to the script without numba, which takes more than one minute to calculate.
the problem arose with numbers greater than 10^9 because numba does not support working with long ints.

In an attempt to solve this problem, I implemented large number arithmetic, but even with numba, due to the large number of operations and transformations, the calculations take too long.

So I decided to cheat and calculate numbers up to 10^9 in a loop, and calculate numbers greater than 10^9 using the formula N(N+1)/2.

---

### Task 2 - Counting islands
You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands, 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.

**Solution ideas:**
The solution is based on finding the total number of connected components in the graph problem. The idea is to start breadth-first search (DFS) at each raw node and increase the number of islands. Each BFS traversal will mark all cells that make up one island as processed. So, the problem comes down to finding the total number of DFS calls.

---

### Task 3 - Regression on the tabular data
You have a dataset (internship_train.csv) that contains 53 anonymized features and a target column. Your task is to build model that predicts a target based on the proposed features. Please provide predictions for internship_hidden_test.csv file. Target metric is RMSE. 
#### The main goal is to provide github repository that contains:
1.jupyter notebook with analysis; 
2.code for modeling (Python 3); 
3.file with model predictions; 
4.readme file;
5.requirements.txt file.

