import numpy as np
import matplotlib.pyplot as plt

# Define the function
def z_function(x, y):  
    return np.sin(5 * x) * np.cos(5 * y) / 5
  
# Gradient calculation
def calculate_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)

# Create grid
x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)
X, Y = np.meshgrid(x, y)

# Evaluate Z on the grid
Z = z_function(X, Y)

# Define the initial positions on the surface
current_position1 = (0.7, 0.4, z_function(0.7, 0.4))
current_position2 = (0.3, 0.8, z_function(0.3, 0.8))
current_position3 = (-0.5, 0.5, z_function(-0.5, 0.5))
learning_rate = 0.05

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8, zorder=0)

# Gradient descent loop
for _ in range(100):  # Adjust the range for desired iterations
    # Update position 1
    x_derivative, y_derivative = calculate_gradient(current_position1[0], current_position1[1])
    x_new1 = current_position1[0] - learning_rate * x_derivative
    y_new1 = current_position1[1] - learning_rate * y_derivative
    current_position1 = (x_new1, y_new1, z_function(x_new1, y_new1))
    
    # Update position 2
    x_derivative, y_derivative = calculate_gradient(current_position2[0], current_position2[1])
    x_new2 = current_position2[0] - learning_rate * x_derivative
    y_new2 = current_position2[1] - learning_rate * y_derivative
    current_position2 = (x_new2, y_new2, z_function(x_new2, y_new2))
    
    # Update position 3
    x_derivative, y_derivative = calculate_gradient(current_position3[0], current_position3[1])
    x_new3 = current_position3[0] - learning_rate * x_derivative
    y_new3 = current_position3[1] - learning_rate * y_derivative
    current_position3 = (x_new3, y_new3, z_function(x_new3, y_new3))
    
    # Clear previous points and re-plot updated points
    ax.scatter(current_position1[0], current_position1[1], current_position1[2], color="red", zorder=1)
    ax.scatter(current_position2[0], current_position2[1], current_position2[2], color="blue", zorder=1)
    ax.scatter(current_position3[0], current_position3[1], current_position3[2], color="green", zorder=1)
    
    plt.pause(0.01)

plt.show()

