from timeit import timeit

setup = 'from count_False_to_True_transitions import count_transitions, x; import numpy as np'
num = 1000
t1 = timeit('count_transitions(x)', setup=setup, number=num)
t2 = timeit('np.count_nonzero(x[:-1] < x[1:])', setup=setup, number=num)
print('Speed difference: {:0.1f}x'.format(t1 / t2))
