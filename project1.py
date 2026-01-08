import requests

BASE_URL = "https://uselessfacts.jsph.pl/random.json?language="

def get_random_fact(language="en"):
    try:
        response = requests.get(f"{BASE_URL}{language}", timeout=5)
        response.raise_for_status()
        fact = response.json()["text"]
        print(f"\n✨ Random Fact ({language.upper()}): {fact}\n")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error: {e}")

def get_filtered_fact(keyword, language="en"):
    print(f"\n🔍 Searching for a fact containing '{keyword}'...\n")
    tries = 0

    while tries < 15:  # limit the search attempts
        try:
            response = requests.get(f"{BASE_URL}{language}", timeout=5)
            response.raise_for_status()
            fact = response.json()["text"]

            if keyword.lower() in fact.lower():
                print(f"✅ Found a '{keyword}' fact:\n{fact}\n")
                return

            tries += 1

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error: {e}")
            return

    print(f"❌ Couldn't find a fact related to '{keyword}' after {tries} tries.\n")

# === Main interactive loop ===
print("=== Exploring Different Endpoints in Facts APIs ===")
print("Choose an option below:\n")

while True:
    print("1️⃣ Get a random fact (English)")
    print("2️⃣ Get a random fact (German)")
    print("3️⃣ Get a filtered fact (e.g., 'computer', 'science', 'internet')")
    print("4️⃣ Quit")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        get_random_fact("en")

    elif choice == "2":
        get_random_fact("de")

    elif choice == "3":
        keyword = input("Enter a keyword to filter by: ").strip()
        if keyword:
            get_filtered_fact(keyword)
        else:
            print("⚠️ Please enter a valid keyword.\n")

    elif choice == "4":
        print("👋 Exiting. Thanks for exploring APIs!")
        break

    else:
        print("⚠️ Invalid choice, please enter 1-4.\n")
