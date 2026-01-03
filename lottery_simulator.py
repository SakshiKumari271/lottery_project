import random

# ---- USER INPUT ----
print("🎟️ Welcome to the Lottery & Probability Simulator")

user_numbers = set()

while len(user_numbers) < 6:
    try:
        num = int(input(f"Enter unique number {len(user_numbers)+1} (1–49): "))
        if 1 <= num <= 49:
            user_numbers.add(num)
        else:
            print("Number must be between 1 and 49.")
    except ValueError:
        print("Please enter a valid number.")

print(f"\nYour ticket numbers: {sorted(user_numbers)}")

# ---- SIMULATION ----
attempts = 0
stats = {}

while True:
    attempts += 1
    winning_numbers = set(random.sample(range(1, 50), 6))

    matches = len(user_numbers.intersection(winning_numbers))

    # Dictionary comprehension logic
    stats[matches] = stats.get(matches, 0) + 1

    match matches:
        case 6:
            print("\n🎉 JACKPOT WON!")
            print(f"Winning numbers: {sorted(winning_numbers)}")
            print(f"Attempts taken: {attempts}")
            break
        case 5:
            pass
        case _:
            pass

# ---- RESULTS ----
print("\n📊 Match Statistics:")
for k, v in sorted(stats.items()):
    print(f"{k} matches → {v} times")
