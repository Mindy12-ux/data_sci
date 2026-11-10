# [XGBoost 문제] 
# kaggle.com이 제공하는 'glass datasets' testdata 폴더 : glass.csv
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7 가지의 label(Type)로 분리된다.

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from xgboost import XGBClassifier

# 데이터
dataset = pd.read_csv('https://raw.githubusercontent.com/Mindy12-ux/python_fork_test/refs/heads/master/testdata_utf8/glass.csv')
print(dataset.head(2))
print(dataset.info())

x = dataset.drop('Type')
y = dataset['Type']

print(x.shpae, y.shape)