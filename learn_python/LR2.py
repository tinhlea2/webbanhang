import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


def LR_use(X, y):

    model = LinearRegression()

    model.fit(X, y)
   
    
    (b_0, b_1,b_2) = (model.intercept_,model.coef_[0],model.coef_[1] )
    y_pred =model.intercept_ + np.sum(model.coef_*x,axis=1)
    print(y_pred)
    plt.plot( y_pred, color = "g")
    plt.show()
    return (b_0, b_1,b_2)

def plot_regression_line(x, y, b):

    # plotting the actual points as scatter plot

    #plt.scatter(x, y, color = "r")

    # predicted response vector
    
    y_pred =b[0] + np.sum(b[1]*x+b[2]*x,axis=1)

    # plotting the regression line
    print(y_pred)
    plt.plot( y_pred, color = "g")

    # putting labels

    plt.xlabel('x')

    plt.ylabel('y')

    # function to show plot

    plt.show()


if __name__ == "__main__":
    #Khởi tạo mảng một chiều với kiểu dữ liệu mặc định
    x = np.array([[0,1],[5,1],[15,2],[25,5],[35,11],[45,15],[55,34],[60,35]])

    y = np.array([4,5,20,14,32,22,38,43])

    #b = LR_coef(x, y)

    b = LR_use(x,y)
    
    #plot_regression_line(x, y, b)
 
