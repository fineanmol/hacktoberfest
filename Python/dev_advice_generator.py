# Developer Advice Generator (in English)
import random
import time

def get_random_advice():
    advices = [
        "Take breaks — your brain needs time to debug itself.",
        "Write code as if the next person maintaining it is a serial killer who knows where you live.",
        "Naming things is hard. Accept it.",
        "Don’t push directly to main. Just… don’t.",
        "A bug in production is worth two in staging.",
        "Your future self will thank you for writing comments today.",
        "Read the error message. Yes, the whole thing.",
        "Before asking for help, try explaining the problem out loud — the rubber duck is your best friend.",
        "Don’t optimize too early — make it work, then make it fast.",
        "Sleep > Coffee > More code.",
        "Commit often, push rarely, regret never.",
        "Tests don’t slow you down — debugging without them does.",
        "The best code is the one you don’t have to write.",
        "AI won’t steal your job. But bad documentation might.",
        "Remember: it’s not a bug, it’s an undocumented feature!"
    ]
    return random.choice(advices)

def main():
    print("💻 Welcome to the Developer Advice Generator 💡")
    time.sleep(1)
    print("\nFetching a random piece of developer wisdom...\n")
    time.sleep(2)
    print(f"👉 {get_random_advice()}")
    print("\nCome back later for more dev wisdom! 🚀")

if __name__ == "__main__":
    main()