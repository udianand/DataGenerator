import random

# Sample lists of client goals, risk levels, investment amounts, and financial advisor responses
client_goals = [
    "to save for retirement and travel",
    "to buy a house in the next 5 years",
    "to fund my child's education",
    "to build an emergency fund",
    "to achieve financial independence",
]

risk_levels = [
    "conservative",
    "moderate",
    "aggressive",
    "balanced",
    "growth-oriented",
]

investment_amounts = [
    "$10,000",
    "$50,000",
    "$100,000",
    "$250,000",
    "$500,000",
]

advisor_responses = [
    "That's an important goal. Let's discuss how investing can help you achieve it.",
    "Considering your goal, it's crucial to align your investment strategy accordingly.",
    "Are you comfortable with taking on more risk to potentially achieve higher returns?",
    "It's great that you have a specific goal in mind. Let's tailor your investment approach to match that.",
    "Based on your goal, we can create a diversified portfolio that suits your risk tolerance.",
    "With your investment amount, we can explore various investment options to meet your objectives.",
    "That's a key consideration. Let's find the right balance between risk and reward for your portfolio.",
]


# Function to generate a random conversation
def generate_otp_call_log() -> str:
    client_goal = random.choice(client_goals)
    risk_level = random.choice(risk_levels)
    investment_amount = random.choice(investment_amounts)
    advisor_response_1 = random.choice(advisor_responses)
    advisor_response_2 = random.choice(advisor_responses)

    conversation = f"**Client:** Hi, I've been thinking about my financial future lately. My goal is {client_goal}. What do you think, should I use an online trading platform?\n\n"
    conversation += f"**FA:** Hello! It's great that you have a specific goal in mind. To help you decide, could you tell me more about your risk tolerance and the amount you're looking to invest?\n\n"
    conversation += f"**Client:** Sure, I have a {risk_level} risk tolerance, and I'm considering investing {investment_amount}.\n\n"
    conversation += f"**FA:** {advisor_response_1}\n\n"
    conversation += f"**Client:** {advisor_response_2}\n\n"

    return conversation


# Generate 10,000 sample conversations
# num_samples = 10
# sample_conversations = [print(generate_sample_conversation()) for _ in range(num_samples)]

# Save the conversations to a file
# with open("sample_conversations.txt", "w") as file:
#    file.writelines(sample_conversations)
