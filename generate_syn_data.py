import pandas as pd
import numpy as np
import random

np.random.seed(42)

N = 10000

education_levels = ["High School", "Bachelor's", "Master's", "PhD"]
careers = ["Engineer", "Artist", "Doctor", "Entrepreneur", "Educator", "Other"]
exercise_levels = ["Rarely", "1-2x/week", "3-5x/week", "Daily"]
locations = ["Urban", "Suburban", "Rural"]

def generate_row():
    age = np.random.randint(18, 66)
    education = random.choice(education_levels)
    career = random.choice(careers)
    sleep = np.round(np.random.normal(7, 1.5), 1)
    sleep = max(4, min(sleep, 10))  # Clamp values
    exercise = random.choice(exercise_levels)
    risk = np.random.randint(0, 11)
    location = random.choice(locations)

    # Simulate target outcomes using a formula
    income = 30000 + age * 400
    income += education_levels.index(education) * 10000
    income += {"Doctor": 40000, "Engineer": 20000, "Entrepreneur": 15000,
               "Artist": -5000, "Educator": 10000, "Other": 0}[career]
    income += risk * 500

    happiness = np.clip(5 + 0.3 * (sleep - 7) + 0.2 * risk + np.random.normal(0, 1), 1, 10)

    health_score = 80
    health_score += {"Rarely": -10, "1-2x/week": 0, "3-5x/week": 5, "Daily": 10}[exercise]
    health_score -= (10 - sleep) * 2
    health_score = np.clip(health_score + np.random.normal(0, 5), 30, 100)

    relationship = np.clip(50 + risk * 3 + np.random.normal(0, 10), 0, 100)

    return {
        "age": age,
        "education": education,
        "career": career,
        "sleep_hours": sleep,
        "exercise": exercise,
        "risk_tolerance": risk,
        "location": location,
        "income_2040": round(income, -2),
        "happiness_score": round(happiness, 1),
        "health_score": int(health_score),
        "relationship_stability": int(relationship)
    }

# Generate dataset
data = [generate_row() for _ in range(N)]
df = pd.DataFrame(data)
df.to_csv("synthetic_life_data.csv", index=False)
print("✅ Synthetic dataset generated and saved as synthetic_life_data.csv")
