import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [200, 220, 250, 270, 300, 320]  # in units
temperature = [30, 35, 40, 45, 50, 55]  # in degrees Fahrenheit

# Create figure and axis
fig, ax1 = plt.subplots()

# Plot the sales data on the first y-axis (only points)
color = 'tab:blue'
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (units)', color=color)
ax1.plot(months, sales, color=color, marker='o', linestyle='None')  # no line
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Temperature (°F)', color=color)
ax2.plot(months, temperature, color=color, marker='x', linestyle='None')  # no line
ax2.tick_params(axis='y', labelcolor=color)

# Add a title and show the plot
plt.title('Monthly Sales and Temperature')
plt.tight_layout()
plt.show()
