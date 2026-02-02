import matplotlib.pyplot as plt
print(plt.style.available)

Rohit=[0,500,800,600,1100,1300,1500,1800,1900,2100]
Kohli = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 900]
Sachin=[500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900,1600]
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]

plt.plot(years,Kohli,color='red',linestyle='--',label="Kohli")
