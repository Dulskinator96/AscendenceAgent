from core.model import query_model
from core.prompt import build_prompt
from memory.memory import store

def run():
    print("AscendenceAgent Initialized\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        prompt = build_prompt(user_input)
        response = query_model(prompt)

        store(user_input + " " + response)

        print("\nAI:", response, "\n")

if __name__ == "__main__":
    run()