
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

tasks = [
    "Planning",
    "Ontology Development",
    "UI Design",
    "Integration",
    "Testing",
    "Documentation"
]

start_dates = [
    "2024-12-01",
    "2024-12-04",
    "2024-12-09",
    "2024-12-12",
    "2024-12-15",
    "2024-12-18"
]

end_dates = [
    "2024-12-03",
    "2024-12-08",
    "2024-12-11",
    "2024-12-14",
    "2024-12-17",
    "2024-12-23"
]

start_dates = [datetime.strptime(date, "%Y-%m-%d") for date in start_dates]
end_dates = [datetime.strptime(date, "%Y-%m-%d") for date in end_dates]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("AI-Powered Smart Gantt Chart Analysis", fontsize=14)

for i, task in enumerate(tasks):
    ax.barh(task, (end_dates[i] - start_dates[i]).days, left=start_dates[i], color="skyblue", edgecolor="black")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.xticks(rotation=45)

plt.xlabel("Timeline")
plt.ylabel("Tasks")
plt.tight_layout()
plt.show()
