import matplotlib.pyplot as plt

players = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs_5yrs = [500+700+1100+1500+1800, 0+200+900+1400+1600, 0+0+500+800+1100, 300+600+800+1100+900]
plt.barh(players,runs_5yrs)
plt.xlabel("Total runs in 5 Year's")
plt.ylabel("Players Name")
plt.title("Firts 5 Years Indian Batsman")
plt.tight_layout()
plt.show()

players = ["Sachin", "Sehwag", "Kohli"]
runs = [1500, 1200, 1800]
plt.bar(players,runs,color="Red")
plt.title("Runs Socred by Players")
for i in range(len(players)):
    plt.text(i,runs[i]+30,str(runs[i]),ha='center')
plt.tight_layout()
plt.show() 