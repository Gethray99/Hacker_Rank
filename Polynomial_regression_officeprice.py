import sys
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def convert_float(x):
    return [float(k) for k in x.strip().split()]

F,N = map(int, sys.stdin.readline().strip().split())
train_data = [convert_float(sys.stdin.readline().strip()) for _ in range(N)]
print(train_data)