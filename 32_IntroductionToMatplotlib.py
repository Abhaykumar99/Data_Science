import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900,1600]

plt.plot(years, runs)
plt.xlabel("Year")
plt.ylabel("Run Scored ")
plt.title("Sachin Tendulkar's Yearly Runs")
plt.show()

Rohit=[0,500,800,600,1100,1300,1500,1800,1900,2100]
Kohli = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 900]

plt.plot(years, Kohli, label="Virat Kohli")
plt.plot(years, Rohit, label="Rohit Sharma")

plt.ylabel("Run Scored")
plt.title("Performance Comparison")
plt.legend()
plt.show()