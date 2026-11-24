# 텐서보드는 머신러닝 실험에 필요한 시각화 및 도구를 제공한다.

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split

from sklearn.datasets import load_diabetes
from torch.utils.tensorboard import SummaryWriter
import datetime

# pip install tensorboard

# data load
diabetes = load_diabetes()
xdata = diabetes.data
ydata = diabetes.target.reshape(-1, 1)
print(xdata[:2], ' ', xdata.shape)                  # (442, 10)
print(ydata[:2], ' ', ydata.shape)                  # (442, 1)
print('feature names : ', diabetes.feature_names)   # ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']


