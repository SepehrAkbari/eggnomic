import numpy as np
import matplotlib.pyplot as plt

def xpart(x, L, b, w):
   numerator = L ** 2 - 4 * (x ** 2)
   denom = L**2 + 8*w*x + 4*w**2
   return (b**2/4)*(numerator/denom)

x = np.linspace(-3, 3, num=50)
y = np.linspace(-3, 3, num=50)
x, y = np.meshgrid(x, y)
X_l3_b2_w0 = xpart(x, L=3, b=2, w=0)
X_l5_b4_w0 = xpart(x, L=5, b=4, w=0)
Y = y**2


fig = plt.figure(figsize=(10, 4))
fig.add_subplot(121)
plt.contourf(Y-X_l3_b2_w0, cmap='magma')
plt.title(r'$L=3, B=2, W=0$', fontsize=12)
fig.add_subplot(122)
plt.title(r'$L=5, B=4, W=0$', fontsize=12)
plt.contourf(Y-X_l5_b4_w0, cmap='magma')
plt.tight_layout()
plt.show()
