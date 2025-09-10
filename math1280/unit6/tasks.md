Assignment Activity:
Context:
Assume you are managing an airport and want to improve passenger flow by studying check-in times. You observe that passengers arriving early for check-in have consistent processing times, while those arriving closer to departure face variability. After closely studying the collected data, you observe the following: 

a. Passengers who arrive within the scheduled check-in period (2 hours before departure) experience uniformly distributed check-in times between 5 and 15 minutes. 

b. For late arrivals, the time it takes for passengers to pass through security and reach the boarding gate follows an exponential distribution with a mean of 10 minutes. 

Using this context, we will address learning objectives and topics related to continuous probability density functions, uniform distribution, and exponential distribution. 

1. Explain what a continuous probability density function is and how it differs from a discrete probability distribution. Use the check-in time data from the airport in your explanation. 
2. What is the probability that a passenger's check-in time is between 7 and 10 minutes, assuming the check-in times are uniformly distributed between 5 and 15 minutes? Provide your solution using appropriate formulas and notations. 
3. What is the probability that a late-arriving passenger will pass through security and reach the gate in less than 5 minutes, assuming an exponential distribution with a mean of 10 minutes? Provide your solution using appropriate formulas and notations.

Answer:
1. **Continuous Probability Density Function**
A continuous probability density function (PDF) is a function that describes the likelihood of a continuous random variable taking on a specific value. Unlike discrete probability distributions, which deal with countable outcomes (e.g., the number of passengers), continuous distributions handle outcomes that can take any value within a range (e.g., time in minutes).
In the context of the airport check-in times, the uniformly distributed check-in times between 5 and 15 minutes represent a continuous random variable. This means that any value within this range is possible, and we can calculate probabilities over intervals rather than for specific values.
2. **Probability of Check-in Time Between 7 and 10 Minutes**
Basically, the uniform distribution is defined by a constant probability over a specified interval. If the check-in times are uniformly distributed between 5 and 15 minutes, probabilities of whole intervals is 1.
So, to find the probability that a passenger's check-in time is between 7 and 10 minutes, we can use the formula for the uniform distribution:
P(X ≤ b) - P(X ≤ a) = (b - a) / (d - c)

Where:
- a = 7 (lower bound)
- b = 10 (upper bound)
- c = 5 (minimum value)
- d = 15 (maximum value)

Substituting these values into the formula gives:

P(7 ≤ X ≤ 10) = (10 - 7) / (15 - 5) = 3 / 10 = 0.3

Therefore, the probability that a passenger's check-in time is between 7 and 10 minutes is 0.3 or 30%.
3. **Probability of Late Arrival Passing Through Security in Less Than 5 Minutes**
To find the probability that a late-arriving passenger will pass through security and reach the gate in less than 5 minutes, we can use the exponential distribution formula:
P(X < x) = 1 - e^(-λx)

Where:
- λ = 1/10 (rate parameter, the inverse of the mean)
- x = 5 (the time threshold)

Substituting these values into the formula gives:

P(X < 5) = 1 - e^(-0.1 * 5) = 1 - e^(-0.5) ≈ 0.3935

Therefore, the probability that a late-arriving passenger will pass through security and reach the gate in less than 5 minutes is approximately 0.3935 or 39.35%.