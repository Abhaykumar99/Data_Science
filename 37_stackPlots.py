import matplotlib.pyplot as plt
activity=["Studying","Playing","Watching TV","Sleepling"]
time_spent=[3,5,4,6]
colors=["red","blue","green","yellow"]
plt.figure(figsize=(6,6))
plt.pie(time_spent,labels=activity,colors=colors,startangle=90,autopct="%1.1f%%")
plt.show()

days = [1, 2, 3, 4, 5, 6, 7]  # Days of the week
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]

labels=['days','studying','tv','sleeping']
colors=['red','pink','orange','skyblue']
plt.figure(figsize=(10,7))
plt.stackplot(days,studying,playing,watching_tv,sleeping,labels=labels,colors=colors,alpha=0.6)
plt.legend(loc="upper right")
plt.grid(True)
plt.title("Weekly Activity Tracker")
plt.xlabel('Day---->')
plt.ylabel("Hours---->")
plt.show()
