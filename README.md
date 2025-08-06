# PRG1: From Pseudocode & Flowcharts to Python

This repository contains Python programs that you will explore using the **PRIMM methodology** (Predict, Run, Investigate, Modify, Make). Each program corresponds to a flowchart and demonstrates key programming concepts.

## 📋 Programs Overview

| Program | Concept | Description |
|---------|---------|-------------|
| `01netflix_binge_sequence.py` | **Sequence** | Calculate binge-watching time |
| `02gaming_achievement_selection.py` | **Selection** | Determine gaming achievements |
| `03spotify_playlist_iteration.py` | **Iteration** | Analyse playlist moods |
| `04social_media_mixed.py` | **Mixed Concepts** | Social media engagement |
| `05food_delivery_mixed.py` | **Mixed Concepts** | Food delivery calculator |

## 🎯 PRIMM Activities

### **P - PREDICT** 📝
Before running each program:
1. Study the corresponding flowchart in the `flowcharts/` folder
2. Read through the Python code
3. **Predict** what will happen when you run it with these inputs:

**Program 1 (Netflix):**
- Series: "Stranger Things"
- Episodes per season: 8
- Seasons: 4
- Episode length: 50 minutes

**Program 2 (Gaming):**
- Score: 12000
- Hours played: 60
- Enemies defeated: 800

**Program 3 (Spotify):**
- Playlist: "My Vibes"
- Songs: 5
- Moods: happy, sad, energetic, happy, chill

### **R - RUN** ▶️
Run each program and check your predictions:
```bash
python 01netflix_binge_sequence.py
python 02gaming_achievement_selection.py
python 03spotify_playlist_iteration.py
```

### **I - INVESTIGATE** 🔍
Answer these questions after running:

**Program 1:**
- How does the program calculate total hours?
- What happens if you enter 0 seasons?

**Program 2:**
- Which condition is checked first in the if-elif chain?
- What achievement would you get with score=6000, hours=15, enemies=500?

**Program 3:**
- How does the counter system work?
- What determines the "Overall mood"?

##
## 📢 Friendly message. 📢 If you have limited programming experience, some of the following tasks might seem hard at this moment in time. Don't worry! Pick and choose!

### **M - MODIFY** ✏️
Make these changes:

**Program 1:**
- Add a calculation for "episodes per day" if watched over a week
- Include a warning if total days > 7

**Program 2:**
- Add a new achievement level: "Legend" (score ≥ 15000 AND hours ≥ 100)
- Add input validation for negative numbers

**Program 3:**
- Add a new mood category: "romantic"
- Calculate and display the most common mood

### **M - MAKE** 🛠️
Create your own programs:

**Sequence Programs:**
1. **YouTube Watch Time Calculator**
   - Input: videos watched, average length
   - Output: total time, equivalent in days

2. **Commute Cost Calculator**
   - Input: distance, fuel price, car efficiency
   - Output: daily/weekly/monthly costs

3. **Pizza Party Planner**
   - Input: guests, slices per person, slices per pizza
   - Output: pizzas needed, total cost

**Selection Programs:**
4. **Grade Calculator**
   - Input: test scores
   - Output: letter grade using if-elif

5. **Cinema Ticket Pricer**
   - Input: age, day of week, time
   - Output: ticket price with discounts

6. **Weather Outfit Suggester**
   - Input: temperature, weather condition
   - Output: clothing recommendations

**Iteration Programs:**
7. **Shopping List Analyser**
   - Input: items and prices
   - Output: total cost, most expensive item

8. **Fitness Tracker**
   - Input: daily steps for a week
   - Output: total steps, average, best day

9. **Book Reading Progress**
   - Input: pages read each day
   - Output: total pages, reading streak

**Mixed Concept Programs:**
10. **Student Timetable Analyser**
    - Input: subjects, hours per week
    - Output: workload assessment, study recommendations

11. **Holiday Budget Calculator**
    - Input: destination, days, daily budget
    - Output: total cost, spending categories

## 🚀 Getting Started

1. Fork this repository
2. Start with the flowcharts to understand the logic
3. Follow the PRIMM activities in order
4. Use Python 3 to run the programs

## 💡 Learning Objectives

By completing these activities, you will:
- Understand sequence, selection, and iteration
- Practice reading and tracing code

Some of you will be able to start:
- Learn to modify existing programs
- Build confidence in writing new programs
- Connect visual flowcharts to Python syntax

## 📁 File Structure
```
├── flowcharts/           # Visual representations
├── 01-05*.py            # Python programs
└── README.md            # This guide
```

---
*Remember: Programming is about problem-solving. Take time to understand each concept before moving to the next!*
