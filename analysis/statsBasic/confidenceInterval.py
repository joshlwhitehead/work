import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import t, norm

x = [0.598,0.606,0.613,0.62,0.628,0.634,0.64,0.645,0.65,0.656,0.66,0.664,0.668,0.671,0.674,0.677,0.679,0.68]


def simple_stats2(sample, alpha):
    mean_er = np.mean(sample) # sample mean
    std_dev_er = np.std(sample, ddof=1) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(sample)) # standard error
    n = len(sample) # sample size, n
    dof = n - 1 # degrees of freedom
    t_star = t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    moe = t_star * se # margin of error
    ci = np.array([mean_er - moe, mean_er + moe])
    print('sample size = {:d}'.format(n))
    print('sample mean = {:.1f} kg/h'.format(mean_er))
    print('sample standard deviation = {:.2f} kg/h'.format(std_dev_er))
    print('standard error = {:.3f} kg/h'.format(se))
    print('t statistic = {:.3f}'.format(t_star))
    print('margin of error = {:.2f} kg/h'.format(moe))
    print('95 % CI for mean = {:.1f}, {:.1f}, kg/h'.format(ci[0], ci[1]))
    return

simple_stats2(x,.05)

print(np.mean(x)-.6)