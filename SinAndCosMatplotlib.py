
# coding: utf-8

# In[18]:

import numpy as np
import matplotlib.pyplot as plt

# Set the figure size to a bigger one
plt.figure(figsize=(15, 8))

# Set the x axis range with linspace and the sin and cos functions
x = np.linspace(-np.pi, np.pi, 200)
y = np.sin(x)
y2 = np.cos(x)

# Plot the sin and cos functions
plt.plot(x, y, color="red", label="sin")
plt.plot(x, y2, color="blue", label="cos")

# Add a padding to the x anx y axis to see the entire figure easily
axisPad = [np.min(x)*1.1, np.max(x)*1.1, np.min(y)*1.1, np.max(y)*1.1]
plt.axis(axisPad)

# Set the grid delimitations
ygrid = [np.min(y), 0,  np.max(y)]
xgrid = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]

# Set the label to the grid delimitation
plt.yticks(ygrid, ('-1', '0', '+1'), fontsize=14)
plt.xticks(xgrid, ('-$\pi$', '-$\pi$/2', '0', "-$\pi$/2", "$\pi$"), fontsize=14)
plt.grid(color='grey', linestyle=':', linewidth=1, alpha=0.5)

# Set the title, legend and xand y label
plt.title("Sin and Cos", fontsize=24)
plt.legend(prop={'size': 18})

plt.xlabel("X", fontsize=20)
plt.ylabel("Y", fontsize=20, rotation=0)


# Show the figure
plt.show()


# In[ ]:



