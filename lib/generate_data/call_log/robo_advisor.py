import random

# Customized lists
financial_goals = [
    "saving for retirement",
    "buying a home",
    "paying off student loans",
    "starting a business",
    "building a diversified portfolio",
    "self_directed_investor",
]

risk_levels = ["conservative", "moderate", "aggressive", "customized", "balanced"]

investment_amounts = ["1000", "5000", "10000", "25000", "50000", "100000"]

other_requirements = [
    "gives tax-loss harvesting for reduced tax liability.",
    "is easy for beginners with minimum financial knowledge.",
    "offers research and recommendations for self-directed investors.",
    "lowers minimum investment requirements compared to some alternatives.",
]

intermediate_responses = ["Awesome", "Sounds good", "Absolutely"]

responses = [
    "That aligns well with your long-term goals.",
    "For that objective, a diversified approach is recommended.",
    "Let's create a tailored investment plan together.",
    "We'll closely monitor market trends on your behalf.",
    "You're taking a proactive step towards financial success!",
]


# Generate 10,000 interactions
def generate_robo_advisor_call_log() -> str:
    goal = random.choice(financial_goals)
    risk_tolerance = random.choice(risk_levels)
    investment_amount = random.choice(investment_amounts)
    intermediate_response = random.choice(intermediate_responses)
    other_requirement = random.choice(other_requirements)
    response = random.choice(responses)

    conversation = "**Financial Advisor (FA):** Hello! I'm your advisor, here to assist you with your financial goals."
    conversation += f"**Individual (I):** Hi! I'm interested in {goal}. I consider myself {risk_tolerance} in terms of risk, and I have ${investment_amount} to allocate."
    conversation += f"**FA:** {intermediate_response}... Any other requirement ?"
    conversation += (
        f"**I:** hmmm, yes, I am looking for something that {other_requirement}"
    )
    conversation += f"**FA:** {response}\n"

    return conversation
