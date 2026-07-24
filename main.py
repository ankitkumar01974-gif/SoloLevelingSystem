
import json
import os
# Load करने का function
def load_data():
    try:
        with open("player.json", "r") as f:
            return json.load(f)
    except:
        return {"name": "", "level": 1, "exp": 0}

# Save करने का function  
def save_data(data):
    with open("player.json", "w") as f:
        json.dump(data, f)

print("=== SOLO LEVELING SYSTEM ===")
data = load_data()

if data["name"] == "":
    data["name"] = input("Apna naam daalo: ")

print(f"\nWelcome {data['name']}!")
print(f"Level: {data['level']} | EXP: {data['exp']}/100")
print("Aaj ka mission: 10 pushup karo")

done = input("\nMission complete kiya? haan/naa: ")
if done == "haan":
    data["exp"] = data["exp"] + 50
    print(f"Badhaai ho! +50 EXP mil gaye")
    if data["exp"] >= 100:
        data["level"] = data["level"] + 1
        data["exp"] = 0
        print(f"LEVEL UP! Ab tum Level {data['level']} ho")
    print(f"Naya EXP: {data['exp']}/100")

save_data(data)
print("\n=== SYSTEM BAND ===")
