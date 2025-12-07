import os
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

USERS = ["Ray", "Hayden", "Arthur"]
CATEGORIES = ["Leetcode", "Neetcode", "Project Euler"]
DISPLAY_NAMES = {"Ray": "Ray", "Hayden": "Hayden", "Arthur": "Arthur"}
CATEGORY_TITLES = {"Leetcode": "LeetCode", "Neetcode": "NeetCode", "Project Euler": "Euler"}

COLORS = {'Ray': '#FF5555', 'Hayden': '#50fa7b', 'Arthur': '#8be9fd'}

VALID_EXTENSIONS = (
    ".py", ".js", ".ts", ".java", ".cpp", ".c", ".cs", ".go", 
    ".rb", ".php", ".swift", ".kt", ".rs", ".sql", ".html", ".css"
)

HISTORY_FILE = 'scripts/history.json'
IMAGES_DIR = 'images'

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

current_stats = {user: {cat: 0 for cat in CATEGORIES} for user in USERS}
total_stats = {user: 0 for user in USERS}

for user in USERS:
    for cat in CATEGORIES:
        path = os.path.join(user, cat)
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(VALID_EXTENSIONS):
                        current_stats[user][cat] += 1
                        total_stats[user] += 1

today_str = datetime.now().strftime('%Y-%m-%d')

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r') as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            history = {"dates": [], "scores": {u: [] for u in USERS}}
else:
    history = {"dates": [], "scores": {u: [] for u in USERS}}

if "dates" not in history: history["dates"] = []
if "scores" not in history: history["scores"] = {u: [] for u in USERS}

if history["dates"] and history["dates"][-1] == today_str:
    for user in USERS:
        if len(history["scores"][user]) > 0:
             history["scores"][user][-1] = total_stats[user]
        else:
             history["scores"][user].append(total_stats[user])
else:
    history["dates"].append(today_str)
    for user in USERS:
        history["scores"][user].append(total_stats[user])

with open(HISTORY_FILE, 'w') as f:
    json.dump(history, f, indent=2)

def setup_dark_mode(figsize=(6,4)):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    ax.grid(True, color='#30363d', linestyle='--', alpha=0.5)
    for spine in ax.spines.values():
        spine.set_color('#30363d')
    ax.tick_params(colors='#c9d1d9')
    return fig, ax

fig, ax = setup_dark_mode((10, 5))
x_dates = [datetime.strptime(d, '%Y-%m-%d') for d in history["dates"]]

for user in USERS:
    if history["scores"][user]:
        ax.plot(x_dates, history["scores"][user], 
                label=DISPLAY_NAMES[user], color=COLORS[user], 
                linewidth=3, marker='o')

ax.set_title('Total Growth Over Time', color='white', fontsize=14, fontweight='bold', pad=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.legend(facecolor='#0d1117', edgecolor='#30363d', labelcolor='white')
plt.tight_layout()
plt.savefig(f'{IMAGES_DIR}/progress_line_chart.png', dpi=120, facecolor=fig.get_facecolor())
plt.close()

for cat in CATEGORIES:
    fig, ax = setup_dark_mode((4, 3))
    counts = [current_stats[u][cat] for u in USERS]
    bar_colors = [COLORS[u] for u in USERS]
    labels = [DISPLAY_NAMES[u] for u in USERS]
    
    bars = ax.bar(labels, counts, color=bar_colors)
    ax.set_title(CATEGORY_TITLES[cat], color='white', fontsize=12, fontweight='bold')
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', color='white', fontweight='bold')

    plt.tight_layout()
    filename = f'graph_{cat.replace(" ", "_").lower()}.png'
    plt.savefig(f'{IMAGES_DIR}/{filename}', dpi=120, facecolor=fig.get_facecolor())
    plt.close()