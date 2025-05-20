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


#Functions to filter
# Function that filters by suncost so cheapest goes firts by world
def get_plants_by_world(world_id, sort_by='Sun_Cost'):
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            if sort_by == 'Sun_Cost':
                sql = "SELECT Plant_Name, Sun_Cost FROM Plants WHERE World_Unlocked_ID = ? ORDER BY Sun_Cost ASC;"
            else:
                sql = "SELECT Plant_Name, Sun_Cost FROM Plants WHERE World_Unlocked_ID = ? ORDER BY Plant_Name ASC;"
            cursor.execute(sql, (world_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
#Function to filter suncost for all plants
def get_all_plants_sorted_by_suncost():
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Plant_Name, Sun_Cost, World_Unlocked_ID FROM Plants ORDER BY Sun_Cost ASC;"
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
#func that sorts all plants by name alphabetically
def get_all_plants_sorted_by_name():
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Plant_Name, Sun_Cost, World_Unlocked_ID FROM Plants ORDER BY Plant_Name ASC;"
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
#func that is the main sorting menu and asks for da stuff
def main_sorting_menu():
    print_header("Plants vs Zombies 2 Database")
    print("\nThis is a database for PvZ2 plants. Choose how you want to sort by:")


    while True:
        print("\nSort Plants By:")
        print("1. View all plants sorted by Sun Cost")
        print("2. View all plants sorted by Name")
        print("3. View plants from a specific world sorted by Sun Cost")
        print("4. View plants from a specific world sorted by Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            plants = get_all_plants_sorted_by_suncost()
            print_header("All Plants by Sun Cost")
            print(f"{'Plant Name':<25} | {'Sun Cost':>8} | {'World':<20}")
            print("-" * 60)
            for name, cost, world_id in plants:
                print(f"{name:<25} | {cost:>8} | {worlds.get(world_id, 'Unknown'):<20}")

        elif choice == '2':
            plants = get_all_plants_sorted_by_name()
            print_header("All Plants by Name")
            print(f"{'Plant Name':<25} | {'Sun Cost':>8} | {'World':<20}")
            print("-" * 60)
            for name, cost, world_id in plants:
                print(f"{name:<25} | {cost:>8} | {worlds.get(world_id, 'Unknown'):<20}")

        elif choice == '3' or choice == '4':
            print_world_glossary()
            try:
                world_id = int(input("Enter World ID: "))
                if world_id not in worlds:
                    raise ValueError()
            except ValueError:
                print("Invalid World ID. Please enter a number from the glossary.")
                continue

            sort_by = 'Sun_Cost' if choice == '3' else 'Plant_Name'
            plants = get_plants_by_world(world_id, sort_by)
            if not plants:
                print(f"No plants found in {worlds[world_id]}")
            else:
                print_header(f"{worlds[world_id]} Plants Sorted by {'Sun Cost' if sort_by == 'Sun_Cost' else 'Name'}")
                print(f"{'Plant Name':<25} | {'Sun Cost':>8}")
                print("-" * 36)
                for name, cost in plants:
                    print(f"{name:<25} | {cost:>8}")

        elif choice == '5':
            print("Exiting program")
            break
        else:
            print("That's not a interger. Please select a number between 1 and 5. NO monkey business like decimals and stuff")


if __name__ == "__main__":
    main_sorting_menu()
