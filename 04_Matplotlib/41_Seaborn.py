import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")
x = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 60])
y = np.sin(x)
 
sns.lineplot(x=x, y=y)
plt.title('Beautiful Line Plot')
plt.show()