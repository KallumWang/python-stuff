'''This is code for a Plant's vs Zombies 2 database by Kallum May 2025'''
import sqlite3

# Header
def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# Align with gaps
def gap(value, width):
    return str(value).ljust(width) if value else "N/A".ljust(width)

# Glossary
worlds = {
    1: "Ancient Egypt", 2: "Pirate Seas", 3: "Wild West", 4: "Frostbite Caves", 5: "Lost City", 6: "Far Future", 
    7: "Dark Ages", 8: "Neon Mixtape Tour", 9: "Jurassic Marsh", 10: "Big Wave Beach", 11: "Modern Day", 12: "Player's House"
}

# Print World ID Glossary
print("World ID Glossary:")
for id, name in worlds.items():
    print(f"{id} = {name}")

# Constants and Variables
DATABASE = 'PVZ2.db'

# Asks the user what world id it is, keeps asking until a valid one is entered
def print_all_Plants():  
    while True:
        try:
            World = int(input("What world id: "))
            if World not in worlds:
                raise ValueError("Invalid world ID.")
            break  # valid input, exit loop
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12 corresponding to a world ID.")

    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Plant_Name, World_Unlocked_ID, Sun_Cost FROM Plants WHERE World_Unlocked_ID = ?;"
        cursor.execute(sql, (World,))
        results = cursor.fetchall()

        if not results:
            print("No plants found for that world.")
        else:
            print_header(f"Plants in {worlds[World]}")
            for plant in results:
                print(f"Plant: {plant[0]}, Sun Cost: {plant[2]}")


# Sorts plants by a chosen attribute
def sort_by(attribute):
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            if attribute not in ['Plant_Name', 'Sun_Cost', 'World_Unlocked_ID']:
                raise ValueError("Invalid attribute to sort by.")
            sql = f"SELECT Plant_Name, Sun_Cost, World_Unlocked_ID FROM Plants ORDER BY {attribute} DESC;"
            cursor.execute(sql)
            results = cursor.fetchall()

            print_header(f"Sorted by {attribute.replace('_', ' ').title()}")
            print(f"{'Plant_Name':<25} {'Sun_Cost':<10} {'World_Unlocked_ID':<15}")
            print("-" * 55)
            for plant in results:
                print(f"{gap(plant[0], 25)} {gap(plant[1], 10)} {gap(plant[2], 15)}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except ValueError as ve:
        print(f"Value error: {ve}")

# Main entry point
if __name__ == "__main__":  
    print_all_Plants()
    # Example usage: sort_by('Sun_Cost')
