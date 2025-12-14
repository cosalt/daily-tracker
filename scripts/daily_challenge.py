import requests
import random
import re
import os
import json
from datetime import datetime

README_FILE = "README.md"
LEETCODE_API = "https://leetcode.com/api/problems/all/"
EULER_URL = "https://projecteuler.net/problem="
START_DATE = datetime(2025, 12, 8)
USED_LEETCODE_FILE = "scripts/used_leetcode.json"
CHALLENGE_HISTORY_FILE = "scripts/challenge_history.json"

def get_day_number():
    now = datetime.now()
    delta = now - START_DATE
    day_num = delta.days + 1
    return max(1, day_num)

def get_euler_problems(day_num):
    problem1 = (day_num - 1) * 2 + 1
    problem2 = (day_num - 1) * 2 + 2
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        r1 = requests.get(f"{EULER_URL}{problem1}", headers=headers, timeout=10)
        match1 = re.search(r'<h2>(.*?)</h2>', r1.text)
        title1 = match1.group(1) if match1 else f"Problem {problem1}"
        
        r2 = requests.get(f"{EULER_URL}{problem2}", headers=headers, timeout=10)
        match2 = re.search(r'<h2>(.*?)</h2>', r2.text)
        title2 = match2.group(1) if match2 else f"Problem {problem2}"
        
        link1 = f"[{title1}]({EULER_URL}{problem1})"
        link2 = f"[{title2}]({EULER_URL}{problem2})"
        
        return f"{link1}<br>{link2}"
    except Exception as e:
        print(f"Euler Error: {e}")
        return f"[Problem {problem1}]({EULER_URL}{problem1})<br>[Problem {problem2}]({EULER_URL}{problem2})"

def load_used_leetcode():
    if os.path.exists(USED_LEETCODE_FILE):
        with open(USED_LEETCODE_FILE, 'r') as f:
            try:
                return json.load(f)
            except:
                return {"easy": [], "medium": [], "hard": []}
    return {"easy": [], "medium": [], "hard": []}

def save_used_leetcode(used):
    os.makedirs(os.path.dirname(USED_LEETCODE_FILE), exist_ok=True)
    with open(USED_LEETCODE_FILE, 'w') as f:
        json.dump(used, f, indent=2)

def load_challenge_history():
    if os.path.exists(CHALLENGE_HISTORY_FILE):
        with open(CHALLENGE_HISTORY_FILE, 'r') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def save_challenge_history(history):
    os.makedirs(os.path.dirname(CHALLENGE_HISTORY_FILE), exist_ok=True)
    with open(CHALLENGE_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def get_leetcode_set():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        
        print("Fetching LeetCode data...")
        r = requests.get(LEETCODE_API, headers=headers, timeout=15)
        r.raise_for_status()
        data = r.json()
    
        print(f"Got {len(data.get('stat_status_pairs', []))} problems")
        
        free_questions = [q for q in data['stat_status_pairs'] if q['paid_only'] is False]
        
        used = load_used_leetcode()
        
        easies = [q for q in free_questions if q['difficulty']['level'] == 1 
                  and q['stat']['question_id'] not in used['easy']]
        mediums = [q for q in free_questions if q['difficulty']['level'] == 2 
                   and q['stat']['question_id'] not in used['medium']]
        hards = [q for q in free_questions if q['difficulty']['level'] == 3 
                 and q['stat']['question_id'] not in used['hard']]
        
        print(f"Available: {len(easies)} easy, {len(mediums)} medium, {len(hards)} hard")
        
        if not easies:
            print("Resetting easy pool")
            used['easy'] = []
            easies = [q for q in free_questions if q['difficulty']['level'] == 1]
        if not mediums:
            print("Resetting medium pool")
            used['medium'] = []
            mediums = [q for q in free_questions if q['difficulty']['level'] == 2]
        if not hards:
            print("Resetting hard pool")
            used['hard'] = []
            hards = [q for q in free_questions if q['difficulty']['level'] == 3]
        
        def format_q(q):
            title = q['stat']['question__title']
            slug = q['stat']['question__title_slug']
            link = f"https://leetcode.com/problems/{slug}/"
            return f"[{title}]({link})", q['stat']['question_id']
        
        easy_choice = random.choice(easies)
        medium_choice = random.choice(mediums)
        hard_choice = random.choice(hards)
        
        e, e_id = format_q(easy_choice)
        m, m_id = format_q(medium_choice)
        h, h_id = format_q(hard_choice)
        
        print(f"Selected: {e}, {m}, {h}")
        
        used['easy'].append(e_id)
        used['medium'].append(m_id)
        used['hard'].append(h_id)
        
        save_used_leetcode(used)
        
        return e, m, h
        
    except Exception as e:
        print(f"LeetCode Error: {e}")
        import traceback
        traceback.print_exc()
        return "[Error loading]", "[Error loading]", "[Error loading]"

def generate_history_section(history):
    if not history:
        return "No previous challenges yet."
    
    history_sorted = sorted(history, key=lambda x: x['day'], reverse=True)
    
    history_display = history_sorted[:30]
    
    markdown = "<details>\n<summary><b>📜 Click to view previous challenges (last 30 days)</b></summary>\n\n"
    markdown += "| Day | Date | Easy | Medium | Hard | Euler |\n"
    markdown += "|:---:|:---:|:---:|:---:|:---:|:---:|\n"
    
    for entry in history_display:
        day = entry['day']
        date = entry['date']
        easy = entry['easy']
        medium = entry['medium']
        hard = entry['hard']
        euler = entry['euler']
        
        markdown += f"| **Day {day}** | {date} | {easy} | {medium} | {hard} | {euler} |\n"
    
    markdown += "\n</details>"
    return markdown

def update_readme(day_num, easy, medium, hard, euler):
    history = load_challenge_history()
    
    today_str = datetime.now().strftime('%Y-%m-%d')
    existing = [h for h in history if h['date'] == today_str]
    
    if existing:
        for h in history:
            if h['date'] == today_str:
                h['easy'] = easy
                h['medium'] = medium
                h['hard'] = hard
                h['euler'] = euler
    else:
        history.append({
            'day': day_num,
            'date': today_str,
            'easy': easy,
            'medium': medium,
            'hard': hard,
            'euler': euler
        })
    
    save_challenge_history(history)
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    start_marker = "<!-- DAILY_CHALLENGE_START -->"
    end_marker = "<!-- DAILY_CHALLENGE_END -->"
    
    neetcode_link = "[NeetCode Practice](https://neetcode.io/practice)"
    
    new_section = (
        f"{start_marker}\n"
        f"### 📅 Daily Challenge - Day {day_num} (Started Dec 8, 2025)\n\n"
        f"| 🟢 Easy | 🟡 Medium | 🔴 Hard | 📐 Project Euler (2/day) | 🚀 NeetCode |\n"
        f"| :---: | :---: | :---: | :---: | :---: |\n"
        f"| {easy} | {medium} | {hard} | {euler} | {neetcode_link} |\n"
        f"{end_marker}"
    )
    
    pattern = f"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
    content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    
    history_start = "<!-- CHALLENGE_HISTORY_START -->"
    history_end = "<!-- CHALLENGE_HISTORY_END -->"
    
    history_section = (
        f"{history_start}\n"
        f"{generate_history_section(history)}\n"
        f"{history_end}"
    )
    
    history_pattern = f"{re.escape(history_start)}.*?{re.escape(history_end)}"
    content = re.sub(history_pattern, history_section, content, flags=re.DOTALL)
    
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("README updated successfully!")

if __name__ == "__main__":
    print("Starting daily challenge update")
    day_num = get_day_number()
    print(f"Day {day_num}")
    
    e, m, h = get_leetcode_set()
    euler = get_euler_problems(day_num)
    
    print(f"Final results:")
    print(f"  Easy: {e}")
    print(f"  Medium: {m}")
    print(f"  Hard: {h}")
    print(f"  Euler: {euler}")
    
    update_readme(day_num, e, m, h, euler)
    print("Done!")