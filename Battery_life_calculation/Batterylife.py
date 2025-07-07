import os 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    timecharged = float(input())
    file = np.loadtxt("trainingdata.txt", delimiter=",")
    file = file[file[:,1]< 8]
    # plt.plot(file[:,0], file[:,1], 'ro', label='Training Data')
    # plt.xlabel('Time Charged (hours)')
    # plt.ylabel('Battery Life (hours)')
    # plt.title('Battery Life vs Time Charged')
    # plt.show()
    
    X = file[:,0].reshape(-1,1)
    y = file[:,1]

    model = LinearRegression()
    model.fit(X, y)

    life_time = model.predict([[timecharged]])
    if life_time[0] > 8:
        life_time[0] = 8
    print(f"{life_time[0]:.2f}")