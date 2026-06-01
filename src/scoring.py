def generate_credit_score(default_probability):
    score = 900 - (default_probability * 600)
    return round(score)


def risk_category(score):
    if score >= 800:
        return "Low Risk"
    elif score >= 650:
        return "Medium Risk"
    return "High Risk"

def recommendation(score):
    if score >= 800:
        return "Approve"
    elif score >= 650:
        return "Review"
    return "Reject"