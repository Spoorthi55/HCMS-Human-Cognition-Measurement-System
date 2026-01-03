def learner_insights(profile):
    insights = []

    if profile["confidence"] > profile["mastery"]:
        insights.append("Learner is overconfident.")
    elif profile["confidence"] < profile["mastery"]:
        insights.append("Learner is underconfident.")

    if profile["consistency"] < 0.7:
        insights.append("Learner responses are unstable.")

    if not insights:
        insights.append("Learner shows healthy cognitive alignment.")

    return insights
