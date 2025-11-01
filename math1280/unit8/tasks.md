Assignment Activities:
You have been assigned to conduct a case study on tourism in the renowned city of Pushkar, a vibrant and culturally rich destination located in northern India. This city attracts visitors from across the globe, celebrating its rich heritage, traditional festivals, and unique cuisine.  

As part of your study, you visit the colorful city to collect and analyze data regarding its economic impact. One key piece of information gathered from city revenue records is the average daily revenue generated from tourists, which amounts to 3.7 million INR, with a standard deviation of 0.52 million INR.  This data sheds light on the financial role tourism plays in Pushkar, making it clear how important it is to the local economy. Your findings could help highlight Pushkar’s economic importance and identify areas for growth.  

The city’s revenue varies significantly during certain months, prompting a study of these fluctuations. To study this, a random revenue data sample of days across multiple years is collected. This study helps in understanding the nature of revenue changes and aids in strategic planning for managing resources during months with notable fluctuations. 

Question:
1. Describe the Central Limit Theorem and discuss associated concepts, such as the Law of Large Numbers and the sampling distribution of sample means, in the context of the given scenario. (ULO 8.1) 

2. Please add the necessary formulas and calculation steps to answer the following questions: 

    a. Based on the Central Limit Theorem, if daily revenue is recorded for a random sample of 30 days in Pushkar City over multiple years, what is the probability that the sample mean revenue falls between 3.5 million INR and 3.8 million INR?

    b. The total revenue of a specific month is 110 million INR. Suppose you are given the revenue data for a random sample of 30 days from multiple years. What is the probability that the total revenue of the 30 random days is less than the revenue of this specific month? Use the provided mean and standard deviation with the sampling distribution of sums to calculate this probability.


Answer:
1. The Central Limit Theorem (CLT) states that the distribution of the sample means will approach a normal distribution as the sample size increases, regardless of the population's distribution, provided the samples are independent and identically distributed (i.i.d.). In the context of Pushkar's tourism revenue, this means that if we take multiple random samples of daily revenue over a period of time, the means of these samples will form a normal distribution centered around the population mean (3.7 million INR) with a standard deviation equal to the population standard deviation divided by the square root of the sample size (0.52 million INR / √30). 

The Law of Large Numbers complements the CLT by stating that as the sample size increases, the sample mean will converge to the population mean. This is important for ensuring that our sample accurately reflects the true average revenue generated from tourism in Pushkar.

The sampling distribution of sample means is the probability distribution of all possible sample means from a population. In this case, it allows us to make inferences about the average daily revenue from a sample of 30 days, helping us understand the overall economic impact of tourism in Pushkar.

2. I will answer the two question like below:
   I have the formula in LateX format. 
    a. To find the probability that the sample mean revenue falls between 3.5 million INR and 3.8 million INR, we first need to calculate the standard error (SE) of the sample mean:

    \[
    SE = \frac{\sigma}{\sqrt{n}} = \frac{0.52}{\sqrt{30}} \approx 0.095
    \]

    Next, we can standardize the values using the z-score formula:

    \[
    z = \frac{\bar{x} - \mu}{SE}
    \]

    For 3.5 million INR:

    \[
    z_{3.5} = \frac{3.5 - 3.7}{0.095} \approx -2.11
    \]

    For 3.8 million INR:

    \[
    z_{3.8} = \frac{3.8 - 3.7}{0.095} \approx 1.05
    \]

    Now, we can use the standard normal distribution table to find the probabilities corresponding to these z-scores:

    \[
    P(Z < -2.11) \approx 0.0174
    \]
    \[
    P(Z < 1.05) \approx 0.8531
    \]

    Therefore, the probability that the sample mean falls between 3.5 million INR and 3.8 million INR is:

    \[
    P(3.5 < \bar{X} < 3.8) = P(Z < 1.05) - P(Z < -2.11) \approx 0.8531 - 0.0174 = 0.8357
    \]

    b. To find the probability that the total revenue of the 30 random days is less than 110 million INR, we first need to calculate the mean and standard deviation of the total revenue:

    Mean of total revenue:

    \[
    \mu_{total} = n \cdot \mu = 30 \cdot 3.7 = 111 \text{ million INR}
    \]

    Standard deviation of total revenue:

    \[
    \sigma_{total} = \sqrt{n} \cdot \sigma = \sqrt{30} \cdot 0.52 \approx 2.84 \text{ million INR}
    \]

    Now, we can standardize the value using the z-score formula:

    \[
    z = \frac{x - \mu_{total}}{\sigma_{total}} = \frac{110 - 111}{2.84} \approx -0.35
    \]

    Using the standard normal distribution table, we find:

    \[
    P(Z < -0.35) \approx 0.3632
    \]

    Therefore, the probability that the total revenue of the 30 random days is less than 110 million INR is approximately 0.3632.

    b. To find the probability that the total revenue of the 30 random days is greater than 115 million INR, we can use the same mean and standard deviation calculated earlier.

    Now, we can standardize the value using the z-score formula:

    \[
    z = \frac{x - \mu_{total}}{\sigma_{total}} = \frac{115 - 111}{2.84} \approx 1.41
    \]

    Using the standard normal distribution table, we find:

    \[
    P(Z < 1.41) \approx 0.9207
    \]

    Therefore, the probability that the total revenue of the 30 random days is greater than 115 million INR is approximately:

    \[
    P(Z > 1.41) = 1 - P(Z < 1.41) \approx 1 - 0.9207 = 0.0793
    \]