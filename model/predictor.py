import numpy as np

def predict_outcomes(features):
    # Fake model using heuristics
    base_income = 30000 + (features['age'] * 500)
    if features['education'] == "PhD":
        base_income += 30000
    elif features['education'] == "Master's":
        base_income += 20000
    elif features['education'] == "Bachelor's":
        base_income += 10000

    if features['career'] == "Doctor":
        base_income += 40000
    elif features['career'] == "Artist":
        base_income -= 10000

    happiness = round(np.clip(5 + 0.2 * features['sleep'] + 0.3 * features['risk'], 1, 10), 1)
    health = "Excellent" if features['exercise'] == "Daily" else "Good" if features['exercise'] == "3-5x/week" else "Average"
    love = int(np.clip(50 + features['risk'] * 3, 0, 100))

    return {
        "income": base_income,
        "happiness": happiness,
        "health": health,
        "love": love
    }
