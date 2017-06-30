import numpy as np
import em

observations = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                         [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                         [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                         [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])

print em.em(observations, [0.6, 0.5])
print em.em(observations, [0.5,0.6])
print em.em(observations, [0.3,0.3])
print em.em(observations, [0.9999,0.00000001])
