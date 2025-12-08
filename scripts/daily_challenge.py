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

def get_day_number():
    now = datetime.now()
    delta = now - START_DATE
    day_num = delta.days + 1
    return max(1, day_num)

def get_euler_problems(day_num):
    problem1 = (day_num - 1) * 2 + 1
    problem2 = (day_num - 1) * 2 + 2
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        r1 = requests.get(f"{EULER_URL}{problem1}", headers=headers)
        match1 = re.search(r'<h2>(.*?)</h2>', r1.text)
        title1 = match1.group(1) if match1 else f"Problem {problem1}"
        
        r2 = requests.get(f"{EULER_URL}{problem2}", headers=headers)
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

def get_leetcode_set():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(LEETCODE_API, headers=headers)
        data = r.json()
        
        free_questions = [q for q in data['stat_status_pairs'] if q['paid_only'] is False]
        
        used = load_used_leetcode()
        
        easies = [q for q in free_questions if q['difficulty']['level'] == 1 
                  and q['stat']['question_id'] not in used['easy']]
        mediums = [q for q in free_questions if q['difficulty']['level'] == 2 
                   and q['stat']['question_id'] not in used['medium']]
        hards = [q for q in free_questions if q['difficulty']['level'] == 3 
                 and q['stat']['question_id'] not in used['hard']]
        
        if not easies:
            used['easy'] = []
            easies = [q for q in free_questions if q['difficulty']['level'] == 1]
        if not mediums:
            used['medium'] = []
            mediums = [q for q in free_questions if q['difficulty']['level'] == 2]
        if not hards:
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
        
        used['easy'].append(e_id)
        used['medium'].append(m_id)
        used['hard'].append(h_id)
        
        save_used_leetcode(used)
        
        return e, m, h
        
    except Exception as e:
        print(f"LeetCode Error: {e}")
        return "Error", "Error", "Error"

def update_readme(day_num, easy, medium, hard, euler):
    """Update README with new daily challenges"""
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
    new_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    day_num = get_day_number()
    print(f"Day {day_num}")
    
    e, m, h = get_leetcode_set()
    euler = get_euler_problems(day_num)
    
    print(f"Generated: Easy={e}, Medium={m}, Hard={h}")
    print(f"Euler: {euler}")
    
    update_readme(day_num, e, m, h, euler)