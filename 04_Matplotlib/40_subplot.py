import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]
y1=[i*2 for i in x]
y2=[i**2 for i in x]

plt.subplot(1,2,1) # (rows, cols, plot_no)
plt.title('Double of x')
plt.plot(x,y1)
plt.xlabel('Number')
plt.ylabel('Double of Number')

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title('Square of x')
plt.xlabel('Number')
plt.ylabel('Square of x')

plt.tight_layout()
plt.show()


# More variations of x
y3 = [i ** 0.5 for i in x]
y4 = [10 - i for i in x]

plt.figure(figsize=(8, 6))  # Optional: make it bigger

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('x * 2')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('x squared')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('sqrt(x)')

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title('10 - x')

plt.tight_layout()
plt.show()





fig, axs=plt.subplots(1,2)
axs[0].plot(x,y1)
axs[0].set_title('x * 2')

axs[1].plot(x,y2)
axs[1].set_title('X Squared')

fig.suptitle('Comparison Plots',fontsize=15)
fig.tight_layout()
fig.savefig('my_plots.png')
plt.show()