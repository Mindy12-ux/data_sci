import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = pd.read_csv('bike_dataset.csv')
print(data.head(3))

x = data.drop(columns=['datetime', 'casual', 'registered', 'count'])
y = data['count']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)

# 모델 만들기
model = RandomForestRegressor(n_estimators=100, random_state=12)
model.fit(x_train, y_train)

# 중요 변수 확인
importance = pd.DataFrame({
    'feature': x_train.columns,
    'importance': model.feature_importances_
}).sort_values(by='importance', ascending=False)

#print(importance)

top_features = importance['feature'].head(7).tolist()
# print(top_features)

x_train_selected = x_train[top_features]
x_test_selected = x_test[top_features]

# 중요 변수로 학습하는 모델 만들기
model2 = RandomForestRegressor(n_estimators=100, random_state=12)
model2.fit(x_train_selected, y_train)
pred = model2.predict(x_test_selected)

# 예측값 / 실제값 출력
result = pd.DataFrame({
    '예측값': pred,
    '실제값': y_test.values
})

# 결정계수
r2 = r2_score(y_test, pred)

print(result.head(10))
print('결정계수:', r2)







