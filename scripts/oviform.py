import numpy as np
import matplotlib.pyplot as plt

def xpart(x: np.ndarray, L: float, b: float, w: float) -> np.ndarray:
   """
   Calculates the x-component of the oviform curve equation.

    x (numpy.ndarray): The x-coordinates for the plot.
    L (float): Length parameter of the oviform curve.
    b (float): Breadth parameter of the oviform curve.
    w (float): Asymmetry parameter (wedge) of the oviform curve.

   Returns: numpy.ndarray: The calculated x-part values.
   """
   numerator = L ** 2 - 4 * (x ** 2)
   denom = L**2 + 8*w*x + 4*w**2
   return (b**2/4)*(numerator/denom)

def plot_model1():
    x = np.linspace(-3, 3, num=50)
    y = np.linspace(-3, 3, num=50)
    x_mesh, y_mesh = np.meshgrid(x, y) 

    X_l3_b2_w0 = xpart(x_mesh, L=3, b=2, w=0)
    X_l5_b4_w0 = xpart(x_mesh, L=5, b=4, w=0)

    Y_squared = y_mesh**2

    fig = plt.figure(figsize=(10, 4))
    
    fig.add_subplot(121) 
    plt.contourf(Y_squared - X_l3_b2_w0, cmap='magma', levels=50) 
    plt.title(r'$L=3, B=2, W=0$', fontsize=12)
    plt.xlabel('x')
    plt.ylabel('y')

    fig.add_subplot(122) 
    plt.title(r'$L=5, B=4, W=0$', fontsize=12)
    plt.contourf(Y_squared - X_l5_b4_w0, cmap='magma', levels=50) 
    plt.xlabel('x')
    plt.ylabel('y')

    plt.tight_layout() 
    plt.show() 

def plot_model2():
    x = np.linspace(-3, 3, num=50)
    y = np.linspace(-3, 3, num=50)
    x_mesh, y_mesh = np.meshgrid(x, y)

    X_l3_b2_w0 = xpart(x_mesh, L=5.5, b=4.2, w=0)
    X_l5_b4_w0 = xpart(x_mesh, L=5.5, b=4.2, w=0.65)
    
    Y_squared = y_mesh**2

    fig = plt.figure(figsize=(10, 4))
    
    fig.add_subplot(121) 
    plt.contourf(Y_squared - X_l3_b2_w0, cmap='magma', levels=50) 
    plt.title(r'$L=5.5, B=4.2, W=0$', fontsize=12)
    plt.xlabel('x')
    plt.ylabel('y')

    fig.add_subplot(122) 
    plt.title(r'$L=5.5, B=4.2, W=0.65$', fontsize=12)
    plt.contourf(Y_squared - X_l5_b4_w0, cmap='magma', levels=50) 
    plt.xlabel('x')
    plt.ylabel('y')

    plt.tight_layout() 
    plt.show() 

if __name__ == "__main__":
    plot_model1()
    plot_model2()