# https://stackoverflow.com/questions/44206600/how-to-conduct-hypothesis-testing-in-python

"""
sample_norm and sample_pareto are basically just arrays of numbers that are sampled from the normal distribution and
from the Pareto distribution, respectively.
In the example, we just test the null hypothesis "sample_norm is distributed normally" against an alternative
"sample_norm is NOT distributed normally" by calling the kstest function with the given 2 arguments.
"""

from scipy.stats import norm, pareto, kstest

n = 1000
sample_norm = norm.rvs(size=1000)  # generate normally distributed random sample
sample_pareto = pareto.rvs(1.0, size=1000)  # sample from some other distribution for comparison

d_norm, p_norm = kstest(sample_norm, norm.cdf)  # test if the sample_norm is distributed normally (correct hypothesis)
d_pareto, p_pareto = kstest(sample_pareto,
                            norm.cdf)  # test if the sample_pareto is distributed normally (false hypothesis)
# As you can see kstest returns the value of the statistic and the p-value. norm.cdf stands for the cumulative
# distribution function of a normal random variable.

print('Statistic values: %.4f, %.4f' % (d_norm, d_pareto))
print('P-values: %.4f, %.4f' % (p_norm, p_pareto))
# This is how you can test if a random sample is normally distributed using the Kolmogorov-Smirnov test.
