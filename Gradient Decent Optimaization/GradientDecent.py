import matplotlib.pyplot as plt
import numpy as np

function = lambda x : x ** 2
x = np.linspace(-2 , 2 , 200)
plt.plot(x , function(x) ) # parabolic function

def derivative(x):
    return 2 * x
    
    def Gradient_Decent(cur_x, precision , learningRate):
    iterations = 0
    x_points = []
    y_points = []
    
    while cur_x > precision and iterations < 1000:
        x_points.append(cur_x)
        y_points.append(function(cur_x))
        cur_x = cur_x - (learningRate * derivative(cur_x))
        iterations += 1

    print("Local minima is :" , cur_x)
    print("Number of iterations took to find out the minima :",iterations)
    plt.plot(x,function(x) , c = 'c')
    plt.scatter(x_points , y_points , c = 'r')
    plt.xlabel("Intercept")
    plt.ylabel("Error")
    
    Gradient_Decent(2,0.001,0.1)
