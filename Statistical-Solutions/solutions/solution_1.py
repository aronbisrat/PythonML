This is a placeholder for Statistical-Solutions/solutions/solution_1.py
import scipy.stats as stats

# Data
normal_tb = 28
normal_total = 600
slum_tb = 96
slum_total = 400

# Proportions
p_normal = normal_tb / normal_total
p_slum = slum_tb / slum_total

# Hypothesis:
# H0: p_slum <= p_normal (TB prevalence in slum is less than or equal to normal)
# H1: p_slum > p_normal (TB prevalence in slum is greater than normal)

# Perform a two-proportion z-test
import statsmodels.api as sm

count = [slum_tb, normal_tb]
nobs = [slum_total, normal_total]
z_stat, p_value = sm.stats.proportions_ztest(count, nobs, alternative='larger')

print(f"Z-statistic: {z_stat:.4f}, P-value: {p_value:.4f}")

# Conclusion
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: TB prevalence in slum area is significantly higher.")
else:
    print("Fail to reject the null hypothesis: No significant difference in TB prevalence.")
                     
