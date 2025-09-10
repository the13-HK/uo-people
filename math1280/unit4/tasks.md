- Assignment Activity
### Question 1:
FreshMart tracks the purchase probabilities of four popular snack types based on historical sales data:
- Chips: P(Chips) = 0.35
- Cookies: P(Cookies) = 0.30
- Nuts: P(Nuts) = 0.20
- Crackers: P(Crackers) = 0.15
Based on the above data, verify that the given probabilities form a valid discrete probability distribution and explain what it means if the probabilities do not sum to 1.

- Answer:
To verify that the given probabilities form a valid discrete probability distribution, we need to check if the sum of all probabilities equals 1.
Let's calculate the sum:
P(Chips) + P(Cookies) + P(Nuts) + P(Crackers) = 0.35 + 0.30 + 0.20 + 0.15 = 1.00
Since the sum is equal to 1, the given probabilities do form a valid discrete probability distribution.
If the probabilities did not sum to 1, it would indicate that there is an error in the probability assignments, as the total probability for all possible outcomes must always equal 1 in a valid probability distribution.Perhaps some other pattern is emerging, or the calculations are wrong.

### Question 2:
FreshMart sells fresh juice in three sizes, with the following prices and customer purchase probabilities: 

- Small Juice: $3.50 (P(Small)=0.4) 
- Medium Juice: $5.00 (P (Medium)=0.35) 
- Large Juice: $7.00 (P(Large)=0.25) 

Based on the above data, calculate the expected value (average revenue) and standard deviation per juice purchase. 
- Answer:
To calculate the expected value (average revenue) and standard deviation per juice purchase, we can use the following formulas:
1. **Expected Value (E)**:  
   E = Σ (Price * Probability)
   
   For FreshMart's juice sizes:
   E = (3.50 * 0.4) + (5.00 * 0.35) + (7.00 * 0.25)
   E = 1.40 + 1.75 + 1.75 = 4.90

2. **Standard Deviation (σ)**:
   σ = √(Σ (Probability * (Price - E)²))
   = √[(0.4 * (3.50 - 4.90)²) + (0.35 * (5.00 - 4.90)²) + (0.25 * (7.00 - 4.90)²)]
   = √[(0.4 * 1.96) + (0.35 * 0.01) + (0.25 * 4.41)]
   = √[0.784 + 0.0035 + 1.1025]
   = √[1.8900]
   = 1.37 (approximately)
### Question 3:
FreshMart's bakery division produces a line of bread with a 90% success rate for quality control. To ensure consistent quality, the bakery independently tests a random sample of 12 loaves. Based on the context, answer the following: 

Calculate the probability that exactly 10 out of the 12 tested loaves meet the quality standard.  

Calculate the probability that at least 8 out of 10 loaves meet the quality standard.

- Answer:
To solve these problems, we can use the binomial probability formula:
P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
where:
- C(n, k) is the binomial coefficient (n choose k)
- p is the probability of success (0.9 for quality control)
- n is the total number of trials (12 loaves tested)
- k is the number of successful trials (loaves meeting quality standard)
1. **Probability that exactly 10 out of 12 loaves meet the quality standard**:
   - n = 12, k = 10, p = 0.9
   - C(12, 10) = 66 (calculated as 12! / (10! * (12-10)!))
   - P(X = 10) = C(12, 10) * (0.9^10) * (0.1^2)
   - P(X = 10) = 66 * (0.3487) * (0.01)
   - P(X = 10) ≈ 0.230
So, the probability that exactly 10 out of 12 loaves meet the quality standard is approximately 0.230 or 23.0%.
2. **Probability that at least 8 out of 10 loaves meet the quality standard**:
   - This can be calculated as P(X ≥ 8)
   - P(X ≥ 8) = P(X = 8) + P(X = 9) + P(X = 10)
   - n = 10, p = 0.9
   - We calculate each probability:
   - P(X = 8) = C(10, 8) * (0.9^8) * (0.1^2)
   - P(X = 9) = C(10, 9) * (0.9^9) * (0.1^1)
   - P(X = 10) = C(10, 10) * (0.9^10) * (0.1^0)
   - C(10, 8) = 45, C(10, 9) = 10, C(10, 10) = 1
   - P(X = 8) = 45 * (0.4305) * (0.01) ≈ 0.193
   - P(X = 9) = 10 * (0.3874) * (0.1) ≈ 0.387
   - P(X = 10) = 1 * (0.3487) * (1) ≈ 0.3487
   - Now, we sum these probabilities: 
   - P(X ≥ 8) = P(X = 8) + P(X = 9) + P(X = 10)
   - P(X ≥ 8) = 0.193 + 0.387 + 0.3487 ≈ 0.9287

So, the probability that at least 8 out of 10 loaves meet the quality standard is approximately 0.9287 or 92.87%.