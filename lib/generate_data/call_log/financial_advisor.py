import random

goals = [
    "Diversify my investment portfolio",
    "Maximize tax efficiency",
    "Plan for early retirement",
    "Create a charitable foundation",
    "Invest in sustainable assets",
]

risk_levels = [
    "Conservative",
    "Moderate",
    "Aggressive",
]

investment_amounts = [
    "$1 million",
    "$5 million",
    "$10 million",
    "$20 million",
    "$50 million",
]

responses = [
    "That's an interesting goal. Let's discuss how we can achieve it.",
    "I understand your concern. Let's analyze the options.",
    "Excellent choice! We'll work on a strategy to reach that goal.",
    "That's a significant amount. We'll need a comprehensive plan.",
    "I'm glad you're thinking about the future. Let's get started.",
]


# Generate 1000 samples
def generate_fa_call_log() -> str:
    individual = "**Individual**"
    advisor = "**FA**"
    goal = random.choice(goals)
    risk_level = random.choice(risk_levels)
    investment_amount = random.choice(investment_amounts)
    response = random.choice(responses)

    conversation = f"{individual}: (Meeting with {advisor}) Good morning, {advisor}. I wanted to meet today to discuss my financial situation and future plans."
    conversation += f"{advisor}: Good morning, {individual}. I'm glad you could make it. Let's start by reviewing your current financial status. Can you tell me more about your assets and any recent changes?"
    conversation += f"{individual}: Of course. My portfolio includes a mix of stocks, bonds, real estate, and some alternative investments. Recently, I've received a significant inheritance, and I'm looking to expand my investment portfolio."
    conversation += f"{advisor}: That's a significant development. We should consider tax implications and how to optimize these new assets. Are there any specific financial goals you'd like to achieve with this inheritance?"
    conversation += f"{individual}: I'm interested in {goal}."
    conversation += f"{advisor}: Great, let's work on a comprehensive wealth management strategy that aligns with your goals. We'll focus on {risk_level} risk and explore strategies to minimize potential taxes. We can also discuss how to diversify your portfolio to manage risk effectively."
    conversation += f"{individual}: Sounds good. I've also been concerned about market volatility. How can we ensure that my portfolio is resilient during economic downturns?"
    conversation += f"{advisor}: Managing risk is essential. We can implement a diversified investment strategy that includes a mix of assets to reduce overall risk. Additionally, we'll set up regular portfolio reviews and adjust your investment allocations as needed to stay aligned with your risk tolerance and long-term goals."
    conversation += f"{individual}: I appreciate your guidance on that. What about my children's education fund and my retirement planning?"
    conversation += f"{advisor}: We can incorporate those objectives into your financial plan. For education funding, we'll explore tax-advantaged savings options. Regarding retirement, we'll analyze your current retirement accounts, project future income needs, and ensure you're on track to retire comfortably."
    conversation += f"{individual}: Thank you, FA. I feel much more confident about my financial future with your expertise and guidance."
    conversation += f"{advisor}: {response}"
    conversation += "\n" + "-" * 50 + "\n"  # Separating interactions with a line

    return conversation
