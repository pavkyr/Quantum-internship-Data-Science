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

so I decided to cheat and calculate numbers up to 10^9 in a loop, and calculate numbers greater than 10^9 using the formula N(N+1)/2.