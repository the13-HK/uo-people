Questions:
Question 1

The following is a dataset containing student test scores:  

45, 62, 75, 85, 90, 93, 95, 95, 100   


Find the range of the given dataset. 
Determine the 1st and 3rd quartiles as well as the 25th, and 50th percentiles.  
Determine the mean, median, mode, variance, and standard deviation. 
Please provide your comments and explain the reasons if you observe any equality between the values obtained in 1(b) and 1(c). Hint: For example, the 50th percentile aligns with the median but not with the 3rd quartile, and similar patterns can be observed elsewhere.


Question 2

Here is a data set that includes the test scores of 25 students from a statistics class: 

72, 88, 94, 119, 85, 91, 77, 84, 75, 79, 83, 80, 87, 70, 76, 82, 93, 78, 89, 95, 86, 90, 73, 92, 81.  


Create a stem-and-leaf plot, histogram, and box plot for the data, including appropriate labels, titles, and identification of potential outliers in each graph.   

Answer:

Question1

a. the range of the dataset is calculated as follows:
Range = Maximum value - Minimum value = 100 - 45 = 55
b. 
The 1st quartile (Q1) is the median of the first half of the data, which is 75.
The 3rd quartile (Q3) is the median of the second half of the data, which is 95.
The 25th percentile is the same as Q1, which is 75.
The 50th percentile is the same as the median, which is 90.

c. 
The mean is calculated as follows:
Mean = (45 + 62 + 75 + 85 + 90 + 93 + 95 + 95 + 100) / 9 = 85.56 (rounded to two decimal places)
The median is the middle value of the sorted dataset, which is 90.
Variance is calculated as follows:
Variance = [(45 - 85.56)² + (62 - 85.56)² + (75 - 85.56)² + (85 - 85.56)² + (90 - 85.56)² + (93 - 85.56)² + (95 - 85.56)² + (95 - 85.56)² + (100 - 85.56)²] / (9 - 1) =  215.56
Standard deviation is the square root of variance:
Standard deviation = √215.56 = 14.68 (rounded to two decimal places)

d. 
The mean (85.56) and median (90) are not equal, indicating that the dataset is not perfectly symmetrical. The mode (95) is also different from both the mean and median, suggesting that there is a concentration of scores at the higher end of the scale. The 50th percentile aligns with the median, but the 3rd quartile (95) is higher than both the mean and median, indicating a right-skewed distribution. This pattern suggests that while the central tendency measures provide a general idea of the dataset, they do not fully capture its distribution characteristics.

Question 2
To create a stem-and-leaf plot, histogram, and box plot for the given dataset, we first need to organize the data.
1. **Stem-and-Leaf Plot**:
   - Stem: Tens place
   - Leaf: Units place
   ```
   Stem | Leaf
   7    | 0 2 3 5 6 7 8
   8    | 0 1 2 3 4 5 6 7 8 9
   9    | 0 1 2 3 4 5
   11   | 9
   ```
2. **Histogram**:
   - Create bins for the data, e.g., 70-74, 75-79, 80-84, 85-89, 90-94, 95-99, 100-104.
   - Count the number of data points in each bin.
   ```
    Bin     | Frequency
    70-74   | 3
    75-79   | 4
    80-84   | 5
    85-89   | 5
    90-94   | 5
    95-99   | 1
    100-104 | 1
   ```
3. **Box Plot**:
   - Create a box plot using the five-number summary (minimum, Q1, median, Q3, maximum).
   - Identify any potential outliers using the IQR (Interquartile Range) method.
    ```
    Minimum: 70
    Q1: 77
    Median: 85
    Q3: 92
    Maximum: 119
   ```

4. **Outliers**:
   - Calculate the IQR: IQR = Q3 - Q1 = 92 - 77 = 15.
   - Determine the lower and upper bounds for outliers:
     - Lower bound: Q1 - 1.5 * IQR = 77 - 22.5 = 54.5
     - Upper bound: Q3 + 1.5 * IQR = 92 + 22.5 = 114.5
   - Any data points below 54.5 or above 114.5 are considered outliers.
   - In this case, the score of 119 is an outlier.