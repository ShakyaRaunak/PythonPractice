import numpy as np

np.random.seed(444)

x = np.random.choice([False, True], size=100000)
print(x)


def count_transitions(x) -> int:
    count = 0
    for i, j in zip(x[:-1], x[1:]):
        if j and not i:
            count += 1
    return count


print(count_transitions(x))

print(np.count_nonzero(x[:-1] < x[1:]))
