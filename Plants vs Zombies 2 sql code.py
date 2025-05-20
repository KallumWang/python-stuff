'''This is code for a Plants vs Zombies 2 database by Kallum May 2025'''
import sqlite3

# Constants
DATABASE = 'PVZ2.db'
worlds = {
    1: "Ancient Egypt", 2: "Pirate Seas", 3: "Wild West", 4: "Frostbite Caves", 5: "Lost City", 6: "Far Future", 
    7: "Dark Ages", 8: "Neon Mixtape Tour", 9: "Jurassic Marsh", 10: "Big Wave Beach", 11: "Modern Day", 12: "Player's House"
}
#all of the functions 
#function for printing the title
def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")
#function for printing the glossary
def print_world_glossary():
    print("World ID Glossary:")
    for id, name in worlds.items():
        print(f"{id:2} = {name}")
#Function which filters plants by world id
def get_plants_by_world(world_id):
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Plant_Name, Sun_Cost FROM Plants WHERE World_Unlocked_ID = ? ORDER BY Sun_Cost;"
            cursor.execute(sql, (world_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
 #function that asks what world id  Keys being sql keys like FK or PK map process the data by applying da functoin to each item of the iterable (list in this case)
def print_all_plants():
    print_world_glossary()
    while True:
        try:
            world_input = f"What world ID ({'/'.join(map(str, worlds.keys()))}): "
            world = int(input(world_input))
            if world not in worlds:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12. No monkey business like decimals and stuff")
#calls the function from earlier and prints the list of plants in the world and tells you if there is none in that world
    plants = get_plants_by_world(world)
    if not plants:
        print("No plants found for that world.")
    else:
        print_header(f"Plants in {worlds[world]}")
        print(f"{'Plant Name':<25} | {'Sun Cost':>8}")
        print("-" * 36)
        for name, cost in plants:
            print(f"{name:<25} | {cost:>8}")

if __name__ == "__main__":
    print_all_plants()
