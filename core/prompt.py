from memory.memory import retrieve

def build_prompt(user_input):
    memories = retrieve(user_input)
    context = " ".join(memories)

    return f"""
You are an adaptive AI system.

Context:
{context}

User Input:
{user_input}

Response:
"""