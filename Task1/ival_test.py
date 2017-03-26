import numpy as np
from visualize_and_preprocess import train_x
from MyKmeans import MyKmeans

k = 8
length = train_x.shape[1]
NUMBER_OF_TESTS = 30
SSE_List = []

for i in range(NUMBER_OF_TESTS):
    centres = np.random.rand(k, length)
    C, idx, SSE = MyKmeans(train_x, k, centres)
    SSE_List.append(SSE)

np.savetxt('test.out', SSE_List, delimiter=',')