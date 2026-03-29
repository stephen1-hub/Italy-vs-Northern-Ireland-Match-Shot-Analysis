# Italy-vs-Northern-Ireland-Match-Shot-Analysis
## Overview

This project analyzes shot data from a football match between Italy and Northern Ireland using Python and data visualization techniques. The goal is to evaluate attacking efficiency, shot quality, and tactical patterns, and translate insights into actionable recommendations.

## Objective

To assess:

Shot volume and efficiency
Shot locations and quality
Player contributions
Tactical strengths and weaknesses

The analysis focuses on turning raw event data into clear, decision-making insights rather than descriptive statistics.

## Data Used

The dataset consists of event-level shot data with the following features:

x, y → Shot coordinates (StatsBomb 120x80 pitch)
shot_type → Outcome (goal, miss, save, block)
team_home → Team indicator (Home/Away)
player → Player taking the shot
body_part → Type of finish (right foot, left foot, head)
Summary:
Italy (Home): 19 shots
Northern Ireland (Away): 8 shots
## Key Findings
1. Shot Volume & Control
Italy generated 70% of total shots (19/27)
Northern Ireland recorded 8 shots, indicating limited attacking presence
2. Finishing Efficiency
Italy: 2 goals (10.5% conversion rate)
Northern Ireland: 0 goals (0% conversion)

Italy created chances consistently but lacked clinical finishing.

3. Shot Outcome Distribution

Italy:

Goals: 2
Saves: 6
Blocks: 5
Misses: 6

Northern Ireland:

Goals: 0
Saves: 1
Blocks: 3
Misses: 4

26% of Italy’s shots were blocked, highlighting strong defensive pressure.

4. Shot Quality & Location
Italy’s goals came from central areas close to goal
Majority of their shots occurred inside or near the penalty area
Northern Ireland’s shots were mostly from less dangerous positions

Italy accessed high-quality zones; Northern Ireland did not.

5. Attacking Profile
Right foot: 67%
Head: 22%
Left foot: 11%

Italy’s attack is heavily right-foot dominant, reducing unpredictability.

6. Key Players
Moise Kean → 5 shots, 1 goal (primary attacking outlet)
Sandro Tonali → 1 goal from midfield

Italy’s attacking output is concentrated among a few players.

## Visualizations
🔹 Shot Maps
Home and away shot maps plotted using mplsoccer
Color-coded outcomes:
🟢 Goal
🔴 Miss
🟠 Block
🟣 Save
🔹 Combined Shot Map
Comparison of both teams on a single pitch
Highlights spatial dominance and shot clustering
🔹 Player Shot Distribution
Bar chart showing number of shots per player
## Tactical Implications
🇮🇹 Italy
Shot Selection Issues
High number of blocked and missed shots
→ Improve shot quality and decision-making
Predictable Attack
67% right-foot usage
→ Add left-footed balance
Low Conversion Efficiency
→ Improve composure in front of goal
🇬🇧 Northern Ireland
Low Chance Creation
→ Increase attacking phases and final-third entries
Poor Shot Quality
→ Focus on central penetration
Defensive Strength
Successfully blocked multiple shots
→ Maintain structure but improve transitions
## Tools & Libraries
Python
Pandas
NumPy
Matplotlib
mplsoccer
