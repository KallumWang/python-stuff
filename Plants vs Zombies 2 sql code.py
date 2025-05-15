'''This is code for a Plant's vs Zombies 2 database by Kallum May 2025'''
#Imports
import sqlite3


# Header
def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# Allign with gaps
def gap(value, width):
    return str(value) if value else "N/A"

# Glossary
worlds = {
    1: "Ancient Egypt",
    2: "Pirate Seas",
    3: "Wild West",
    4: "Frostbite Caves",
    5: "Lost City",
    6: "Far Future",
    7: "Dark Ages",
    8: "Neon Mixtape Tour",
    9: "Jurassic Marsh",
    10: "Big Wave Beach",
    11: "Modern Day",
    12: "Player's House"
}

print("World ID Glossary:")
for id, name in worlds.items():
    print(f"{id} = {name}")

#Constants and Variables
DATABASE = 'PVZ2.db'
#Asks the user what world id it is
def print_all_Plants():  
    World = input("What world id: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Plant_Name, World_Unlocked_ID, Sun_Cost FROM Plants WHERE World_Unlocked_ID = ?;"
        cursor.execute(sql,(World,))
        results = cursor.fetchall()
        # PRINTS THE DATA NICER
        for Plants in results:
            print(f"Plants: {Plants[0]} Sun_Cost: {Plants[2]}")

if __name__ == "__main__":  
    print_all_Plants()
