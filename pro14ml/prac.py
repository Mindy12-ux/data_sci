import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

np.random.seed(123)

var = ['x', 'y']
labels = ['점0','점1','점2','점3','점4']
x = np.random.random_sample([5,2]) * 10
df = pd.DataFrame(x, columns=var, index=labels)

from scipy.cluster.hierarchy import linkage     # 응집형 계층적 클러스터링
row_clusters = linkage(df, method='ward')
df2 = pd.DataFrame(row_clusters, columns=['군집id1','군집id2','거리', '군집멤버'])
print(df2)