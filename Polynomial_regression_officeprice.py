import sys
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def convert_float(x):
    return [float(k) for k in x.strip().split()]

F,N = map(int, sys.stdin.readline().strip().split())
train_data = [convert_float(sys.stdin.readline().strip()) for _ in range(N)]
X_train = [i[:-1] for i in train_data]
y_train = [i[-1] for i in train_data]
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X_train)
model = LinearRegression()
model.fit(X_poly, y_train)

num_rows = int(sys.stdin.readline().strip())
for _ in range(num_rows):
    x_test = convert_float(sys.stdin.readline().strip())
    x_poly = poly.transform([x_test])
    y_pred = model.predict(x_poly)
    print(f"{y_pred[0]:.2f}")  