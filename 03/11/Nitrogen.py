import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.lines as mlines

# Input data
data = [
    ('03/11/2024', 1.08, 50.6, 6.8),
    ('03/11/2024', 0.8, 45.4, 7.7),
    ('03/25/2024', 1.33, 50, 8.1),
    ('03/25/2024', 1.11, 52.7, 7.3),
    ('04/08/2024', 1.17, 38, 7.5),
    ('04/08/2024', 1.07, 36.9, 7.6),
    ('04/15/2024', 0.58, 48.1, 8.8),
    ('04/15/2024', 1.59, 48.6, 8.4),
]

# Group data by date
grouped = defaultdict(list)
for date, n, moisture, ph in data:
    grouped[date].append((n, moisture, ph))

# Plotting
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Custom color map
color_map = {
    '03/11/2024': 'blue',
    '03/25/2024': 'orange',
    '04/08/2024': 'green',
    '04/15/2024': 'red',
}

# Plot data with hollow markers (no individual labels)
for date, records in grouped.items():
    nitrogen = [r[0] for r in records]
    moisture = [r[1] for r in records]
    ph = [r[2] for r in records]
    color = color_map[date]

    ax1.scatter(nitrogen, moisture, color=color, marker='x', linewidths=1.5)
    ax2.scatter(nitrogen, ph, edgecolors=color, facecolors='none', marker='o', linewidths=1.5)

# Custom legend: one entry per date, plus marker explanation
legend_elements = [
    # Date-color legend entries
    mlines.Line2D([], [], color='blue', marker='o', linestyle='None', label='03/11/2024'),
    mlines.Line2D([], [], color='orange', marker='o', linestyle='None', label='03/25/2024'),
    mlines.Line2D([], [], color='green', marker='o', linestyle='None', label='04/08/2024'),
    mlines.Line2D([], [], color='red', marker='o', linestyle='None', label='04/15/2024'),

    # Marker shape legend entries
    mlines.Line2D([], [], color='black', marker='x', linestyle='None', label='x = Moisture'),
    mlines.Line2D([], [], color='black', marker='o', linestyle='None', markerfacecolor='none', label='o = pH'),
]

# Show legend
ax1.legend(handles=legend_elements, title='Legend', loc='center left', bbox_to_anchor=(1.2, 0.75))

# Axis labels and title
ax1.set_xlabel('Nitrogen (%)')
ax1.set_ylabel('Moisture (%)')
ax2.set_ylabel('pH (1:2)')
plt.title('Moisture and pH vs Nitrogen (%) by Date')

plt.tight_layout()
plt.show()
