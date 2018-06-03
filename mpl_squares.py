import matplotlib.pyplot as plt

input_values = list(range(-1001,1001))
squares = [x**3 for x in input_values]
plt.scatter(input_values,squares,c=squares,cmap=plt.cm.Blues, edgecolor='none',s=2)
#plt.plot(input_values,squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both',labelsize=14)

plt.axis([-1001,1001,-1100000000,1100000000])

plt.show()
