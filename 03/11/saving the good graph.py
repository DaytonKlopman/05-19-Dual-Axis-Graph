import matplotlib.pyplot as plt
from collections import defaultdict

# Input data
data = [
    ('03/11/2024', 1.08, 50.6, 6.8),
    ('03/11/2024', 0.8, 45.4, 7.7),
    ('03/25/2024', 1.33, 50, 8.1),
    ('03/25/2024', 1.11, 52.7, 7.3),
    ('04/08/2024', 1.17, 38, 7.5),
    ('04/08/2024', 1.07, 36.9, 7.6),
    ('04/15/2024', 0.58, 481, 8.8),
    ('04/15/2024', 1.59, 48.6, 8.4),
]

# Group data by date
grouped = defaultdict(list)
for date, n, moisture, ph in data:
    grouped[date].append((n, moisture, ph))

# Plotting
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Color cycle for each date
colors = plt.cm.tab10.colors
color_map = {date: colors[i % len(colors)] for i, date in enumerate(grouped)}

# Plot data with hollow markers
for date, records in grouped.items():
    nitrogen = [r[0] for r in records]
    moisture = [r[1] for r in records]
    ph = [r[2] for r in records]
    color = color_map[date]

    # Hollow X for moisture
    ax1.scatter(nitrogen, moisture, color=color, marker='x', linewidths=1.5, label=f'{date} - Moisture')

    # Hollow circle for pH
    ax2.scatter(nitrogen, ph, edgecolors=color, facecolors='none', marker='o', linewidths=1.5, label=f'{date} - pH')

# Axis labels and title
ax1.set_xlabel('Nitrogen (%)')
ax1.set_ylabel('Moisture (%)', color='tab:blue')
ax2.set_ylabel('pH (1:2)', color='tab:red')
plt.title('Moisture and pH vs Nitrogen (%) by Date')

# Combine and position legends
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.tight_layout()
plt.show()
