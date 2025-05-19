import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.lines as mlines

# Heat compost data from each sample date
data = [
    ('03/11/2024', 42, 50.6, 6.8),
    ('03/11/2024', 45, 45.4, 7.7),
    ('03/25/2024', 58, 50, 8.1),
    ('03/25/2024', 34, 52.7, 7.3),
    ('04/08/2024', 33, 38, 7.5),
    ('04/08/2024', 53, 36.9, 7.6),
    ('04/15/2024', 33, 48.1, 8.8),
    ('04/15/2024', 69, 48.6, 8.4),
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
for date, records in grouped.items():
    zinc = [r[0] for r in records]
    moisture = [r[1] for r in records]
    ph = [r[2] for r in records]
    color = color_map[date]

    ax1.scatter(zinc, moisture, color=color, marker='x', linewidths=1.5)
    ax2.scatter(zinc, ph, edgecolors=color, facecolors='none', marker='o', linewidths=1.5)

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
ax1.set_xlabel('Zinc (ppm)')
ax1.set_ylabel('Moisture (%)')
ax2.set_ylabel('pH (1:2)')
plt.title('Moisture/pH differences in Zinc Samples')

plt.tight_layout()
plt.show()