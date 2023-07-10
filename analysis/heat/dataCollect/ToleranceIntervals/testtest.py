from more_itertools import batched
import numpy as np
josh = [1,2,3,4,5,6]
tess = list(batched(josh,2))
print(np.array(tess))
tess.pop()
print(tess)