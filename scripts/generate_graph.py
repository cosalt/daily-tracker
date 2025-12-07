import os
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# config
USERS = ["Ray", "Hayden", "Arthur"]
CATEGORIES = ["leetcode", "neetcode", "project Euler"]
DISPLAY_NAMES = {"ray": "Ray", "hayden": "Hayden", "arthur": "Arthur"}
CATEGORY_TITLES = {"leetcode": "LeetCode", "neetcode": "NeetCode", "project Euler": "Euler"}

# color Ray (red), Hayden (green), Arthur (blue)
COLORS = {'ray': '#FF5555', 'hayden': '#50fa7b', 'arthur': '#8be9fd'}

# file extensions to validate
VALID_EXTENSIONS = (
    ".py", ".js", ".ts", ".java", ".cpp", ".c", ".cs", ".go", 
    ".rb", ".php", ".swift", ".kt", ".rs", ".sql", ".html", ".css"
)

HISTORY_FILE = 'scripts/history.json'
IMAGES_DIR = 'images'

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

# data
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

# his story
today_str = datetime.now().strftime('%Y-%m-%d')
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)
else:
    history = {"dates": [], "scores": {u: [] for u in USERS}}

# logic
if history["dates"] and history["dates"][-1] == today_str:
    for user in USERS:
        history["scores"][user][-1] = total_stats[user]
else:
    history["dates"].append(today_str)
    for user in USERS:
        history["scores"][user].append(total_stats[user])

with open(HISTORY_FILE, 'w') as f:
    json.dump(history, f, indent=2)

# plot helper

def setup_dark_mode():
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 4))
    # github grey
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    ax.grid(True, color='#30363d', linestyle='--', alpha=0.5)
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['top'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['right'].set_color('#30363d')
    ax.tick_params(axis='x', colors='#c9d1d9')
    ax.tick_params(axis='y', colors='#c9d1d9')
    return fig, ax

# chart main
fig, ax = setup_dark_mode()
fig.set_size_inches(10, 5)

x_dates = [datetime.strptime(d, '%Y-%m-%d') for d in history["dates"]]

for user in USERS:
    ax.plot(x_dates, history["scores"][user], 
            label=DISPLAY_NAMES[user], color=COLORS[user], 
            linewidth=3, marker='o')

ax.set_title('Total Growth Over Time', color='white', fontsize=14, fontweight='bold', pad=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.legend(facecolor='#0d1117', edgecolor='#30363d', labelcolor='white')
plt.tight_layout()
plt.savefig(f'{IMAGES_DIR}/progress_line_chart.png', dpi=120, facecolor=fig.get_facecolor())
plt.close()

# bar chart
for cat in CATEGORIES:
    fig, ax = setup_dark_mode()
    fig.set_size_inches(4, 3) #smaller
    
    counts = [current_stats[u][cat] for u in USERS]
    bar_colors = [COLORS[u] for u in USERS]
    labels = [DISPLAY_NAMES[u] for u in USERS]
    
    bars = ax.bar(labels, counts, color=bar_colors)
    
    ax.set_title(CATEGORY_TITLES[cat], color='white', fontsize=12, fontweight='bold')
    
    # bar top num
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', color='white', fontweight='bold')

    plt.tight_layout()
    # save
    filename = f'graph_{cat.replace(" ", "_").lower()}.png'
    plt.savefig(f'{IMAGES_DIR}/{filename}', dpi=120, facecolor=fig.get_facecolor())
    plt.close()