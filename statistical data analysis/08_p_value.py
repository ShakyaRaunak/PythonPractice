# https://www.tutorialspoint.com/python/python_p_value.htm

"""
The p-value is about the strength of a hypothesis. We build hypothesis based on some statistical model and compare the model's validity
using p-value. One way to get the p-value is by using T-test.
This is a two-sided test for the null hypothesis that the expected value (mean) of a sample of independent observations ‘a’ is
equal to the given population mean, popmean.
"""

from scipy import stats

rvs = stats.norm.rvs(loc=5, scale=10, size=(50, 2))
print(stats.ttest_1samp(rvs, 5.0))
print()

"""
Comparing two samples :
test whether two samples, which can come either from the same or from different distribution, have the same statistical properties.
ttest_ind => calculates the T-test for the means of two independent samples of scores. 
This is a two-sided test for the null hypothesis that two independent samples have identical average (expected) values. 
This test assumes that the populations have identical variances by default.
"""
rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=500)
print(stats.ttest_ind(rvs1, rvs2))
