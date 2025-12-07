import os
import matplotlib.pyplot as plt

# config
USERS = ["Ray", "Hayden", "Arthur"]
DISPLAY_NAMES = ["Ray", "Hayden", "Arthur"]
CATEGORIES = ["leetcode", "neetcode", "project Euler"]

# file types
VALID_EXTENSIONS = (
    ".py", ".js", ".ts", ".java", ".cpp", ".c", ".cs", ".go", 
    ".rb", ".php", ".swift", ".kt", ".rs", ".sql", ".html", ".css"
)

COLORS = ['#3498db', '#e74c3c', '#2ecc71'] 

if not os.path.exists('images'):
    os.makedirs('images')

# data
data = {user: {cat: 0 for cat in CATEGORIES} for user in USERS}
totals = {user: 0 for user in USERS}

for user in USERS:
    for cat in CATEGORIES:
        path = os.path.join(user, cat)
        
        file_count = 0
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(VALID_EXTENSIONS):
                        file_count += 1
                        
        data[user][cat] = file_count
        totals[user] += file_count

# plot
def create_chart(title, counts, filename, color_set=None):
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(DISPLAY_NAMES, counts, color=COLORS if color_set is None else color_set)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylabel('Problems Solved')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=120)
    plt.close()

# graf grap grafh graphs
lc_counts = [data[u]['leetcode'] for u in USERS]
create_chart('LeetCode Standings', lc_counts, 'graph_leetcode.png')

nc_counts = [data[u]['neetcode'] for u in USERS]
create_chart('NeetCode Standings', nc_counts, 'graph_neetcode.png')

pe_counts = [data[u]['project Euler'] for u in USERS]
create_chart('Project Euler Standings', pe_counts, 'graph_euler.png')

total_counts = [totals[u] for u in USERS]
create_chart('TOTAL PROBLEMS SOLVED', total_counts, 'graph_total.png', color_set=['#8e44ad', '#8e44ad', '#8e44ad'])