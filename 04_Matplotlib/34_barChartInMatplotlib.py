import matplotlib.pyplot as plt
import numpy as np

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

plt.bar(years,runs)
plt.xlabel('years')
plt.ylabel('runs')
plt.title("Sachin Tendulakar Yearly Runs")
plt.legend()
plt.show()

sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

x=np.arange(len(years))
print(x)
width=0.25

plt.bar(x-width,sachin,width=width,label='Sachin')
plt.bar(x,kohli,width=width,label="Kohli")
plt.bar(x+width,sehwag,width=width,label="Sehwag")
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Run Comparission")
plt.xticks(x,years)
plt.legend()
plt.tight_layout()
plt.show()