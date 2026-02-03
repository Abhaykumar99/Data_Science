import matplotlib.pyplot as plt

plt.style.use("ggplot")
# Data
labels = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs = [18000, 8000, 12000, 9500]


plt.pie(runs,labels=labels)
plt.title("Career Runs of Indian Batsman")
plt.show()

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(runs, labels=labels, colors=colors)
plt.show()

plt.pie(
    runs,
    labels=labels,
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': '--'}
)
plt.show()

explode=[0.1,0,0,0]
plt.pie(runs,labels=labels,explode=explode,colors=colors,shadow=True,startangle=90,autopct='%1.1f%%')
plt.title("Exploded Pie Example")
plt.tight_layout()
plt.show()

# Too many categories
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'Ruby', 'Go', 'Rust', 'Swift', 'PHP']
usage = [30, 20, 10, 10, 7, 5, 4, 3, 2, 1]

plt.pie(usage, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title("Programming Language Usage (Crowded Example)")
plt.tight_layout()
plt.show()

