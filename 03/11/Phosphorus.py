import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.lines as mlines

# Heat compost data from each sample date
data = [
    ('03/11/2024', 0.24, 50.6, 6.8),
    ('03/11/2024', 0.25, 45.4, 7.7),
    ('03/25/2024', 0.39, 50, 8.1),
    ('03/25/2024', 0.20, 52.7, 7.3),
    ('04/08/2024', 0.19, 38, 7.5),
    ('04/08/2024', 0.28, 36.9, 7.6),
    ('04/15/2024', 0.19, 48.1, 8.8),
    ('04/15/2024', 0.42, 48.6, 8.4),
]

# Group data by date
grouped = defaultdict(list)
for date, n, moisture, ph in data:
    grouped[date].append((n, moisture, ph))

# Moisture and pH X-axis
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Color matching dates under Legend
color_map = {
    '03/11/2024': 'blue',
    '03/25/2024': 'orange',
    '04/08/2024': 'green',
    '04/15/2024': 'red',
}

# Markers for data points
for date, points in grouped.items():
    phosphorus = [r[0] for r in points]
    moisture = [r[1] for r in points]
    ph = [r[2] for r in points]
    color = color_map[date]

    ax1.scatter(phosphorus, moisture, color=color, marker='x', linewidths=1.5)
    ax2.scatter(phosphorus, ph, edgecolors=color, facecolors='none', marker='o', linewidths=1.5)

# Giving color and marker to date(s)
legend_elements = [
    # Date-color legend entries
    mlines.Line2D([], [], color='blue', marker='o', linestyle='None', label='03/11/2024'),
    mlines.Line2D([], [], color='orange', marker='o', linestyle='None', label='03/25/2024'),
    mlines.Line2D([], [], color='green', marker='o', linestyle='None', label='04/08/2024'),
    mlines.Line2D([], [], color='red', marker='o', linestyle='None', label='04/15/2024'),

    # Giving specific markers to Moisture and pH
    mlines.Line2D([], [], color='black', marker='x', linestyle='None', label='x = Moisture'),
    mlines.Line2D([], [], color='black', marker='o', linestyle='None', markerfacecolor='none', label='o = pH'),
]

# Legend
ax1.legend(handles=legend_elements, title='Legend', loc='center left', bbox_to_anchor=(1.2, 0.75))

# Axis labels and title
ax1.set_xlabel('Phosphorus (%)')
ax1.set_ylabel('Moisture (%)')
ax2.set_ylabel('pH (1:2)')
plt.title('Moisture/pH differences in Phosphorus Samples')

plt.tight_layout()
plt.show()