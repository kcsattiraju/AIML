import numpy as np
import matplotlib.pyplot as plt

def  y_function(x):
  return x**2

def y_derivative(x):
 return  x*2
    
x= np.arange(-5,5,0.1)
y = y_function(x)

learning_rate = 0.1 
current_location = (1.5,y_function(1.5))

for p in range(1000):  
    x_new = current_location[0] - learning_rate*current_location[1]
    y_new = y_function(x_new)
    current_location = (x_new,y_new)

    plt.plot(x,y)
    plt.scatter(current_location[0],current_location[1],c="red")
    plt.pause(0.001)
    
    
