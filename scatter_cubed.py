import matplotlib.pyplot as plt 

# Set x and y values
x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

#Plot style
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Plot labels
ax.set_title("Cubed Values", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubed Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

#Plot range
ax.axis([0, 5000, 0, 110000000000])

plt.show()