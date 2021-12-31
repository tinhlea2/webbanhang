import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

def LR_coef(x, y):

    n = np.size(x)

    m_x = np.mean(x) #Trung bình cộng của tất cả các phần tử trong mảng arr.

    m_y = np.mean(y) #Trung bình cộng của tất cả các phần tử trong mảng arr.

    SS_xy = np.sum(y*x) - n*m_y*m_x

    SS_xx = np.sum(x*x) - n*m_x*m_x

    b_1 = SS_xy / SS_xx

    b_0 = m_y - b_1*m_x

    return (b_0, b_1)

def LR_use(X, y):

    model = LinearRegression()

    model.fit(X.reshape(-1, 1), y.reshape(-1, 1))

    (b_0, b_1) = (model.coef_[0][0], model.intercept_[0])

    return (b_0, b_1)

def plot_regression_line(x, y, b):

    # plotting the actual points as scatter plot

    plt.scatter(x, y, color = "r", marker = "o", s = 30)

    # predicted response vector

    y_pred = b[0] + b[1]*x

    # plotting the regression line

    plt.plot(x, y_pred, color = "g")

    # putting labels

    plt.xlabel('x')

    plt.ylabel('y')

    # function to show plot

    plt.show()


if __name__ == "__main__":
    #Khởi tạo mảng một chiều với kiểu dữ liệu mặc định
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    y = np.array([0, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    #b = LR_coef(x, y)

    b = LR_use(x,y)
    
    plot_regression_line(x, y, b)