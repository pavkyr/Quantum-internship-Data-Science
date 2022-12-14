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
1. jupyter notebook with analysis; 
2. code for modeling (Python 3); 
3. file with model predictions; 
4. readme file;
5. requirements.txt file.

**Solution ideas:**
After the initial analysis, the data turned out to be numerical and clean (no gaps, no outliers). Before building the model, it was decided to take a closer look at the influence of features on the target. Using mutual_info_regression from sklearn.feature_selection, the 2 most important features were identified. Feature 6 turned out to be a quadratic function f(x)=x^2, while feature 7 and others were noise.

To build the model, I added polynomial features using PolynomialFeatures from sklearn.preprocessing and used LinearRegression from sklearn.linear_model.
RMSE: 0.0832.

---

### Task 4 - Soil erosion detection
Here is one of the open problems in Quantum. Soil erosion is a really unwanted process that spoils huge areas of fertile land. Your task is to train model for erosion detection.
#### What should we get:
1. jupyter notebook with data analysis;
2. script for model training (preferably tf.keras);
3. readme file;
4. requirements.txt file;
5. solution report.

**solution report:**
The solution to the problem was not received due to incomprehensible crashes of Google Collab. The erosion detection method in this task is entirely based on remote sensing methods and is relatively easy to use. The required data for each factor for the model can be obtained directly from the satellite imagery. The main task at the first stages is to qualitatively mark the necessary zones. The results obtained with this method will be useful to decision makers when developing future soil conservation strategies to reduce soil loss.
To improve the result, it would be nice to have a well-filled .sp file, because a lot of values ??????are missing, we had to artificially generate new data in order to increase the sample size. The resulting .png files had different sizes, which is why they had to be reduced to the same size so that the model could work, which leads to loss of information. In my opinion, masking should be done in approximately the same size, close to a square shape.
This would make it easier to work with the data.
