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


# ANSI escape sequences for 256 colours
RESET = "\033[0m"
BOLD = "\033[1m"

# 256-colour codes for requested colours
COLOUR_GOLD = "\033[38;5;220m"         # Gold (Ancient Egypt)
COLOUR_DARK_BLUE = "\033[38;5;19m"     # Dark Blue (Pirate Seas)
COLOUR_LIGHT_BROWN = "\033[38;5;180m"  # Light Brown (Wild West)
COLOUR_PURPLE = "\033[38;5;93m"        # Purple (Far Future)
COLOUR_GREY = "\033[38;5;244m"         # Grey (Dark Ages)
COLOUR_LIGHT_BLUE = "\033[38;5;117m"   # Light Blue (Big Wave Beach)
COLOUR_DEEP_GREEN = "\033[38;5;28m"    # Dank Green Grass (Modern Day)
COLOUR_LIGHT_GREEN = "\033[38;5;120m"  # Light Green (Player's House)

# Other ANSI colours for fallback or other worlds
COLOUR_CYAN = "\033[36m"   #Cyan (Frost Bite Caves)
COLOUR_MAGENTA = "\033[35m" #Magenta (Neon mixtape tour)
COLOUR_RED = "\033[31m"     #Red (Used for exit program colour)
COLOUR_YELLOW = "\033[33m"  #Yellow (Lost city)
COLOUR_GREEN = "\033[32m"   # green (used for options)
COLOUR_WHITE = "\033[37m"   #White (Incase I need)

# Map world IDs to their colour codes
world_colours = {
    1: COLOUR_GOLD,           # Ancient Egypt
    2: COLOUR_DARK_BLUE,      # Pirate Seas
    3: COLOUR_LIGHT_BROWN,    # Wild West
    4: COLOUR_CYAN,           # Frostbite Caves (kept cyan as before)
    5: COLOUR_YELLOW,         # Lost City (left yellow, you can change)
    6: COLOUR_PURPLE,         # Far Future
    7: COLOUR_GREY,           # Dark Ages
    8: COLOUR_MAGENTA,        # Neon Mixtape Tour (left magenta)
    9: COLOUR_CYAN,           # Jurassic Marsh (kept cyan)
    10: COLOUR_LIGHT_BLUE,    # Big Wave Beach
    11: COLOUR_DEEP_GREEN,    # Modern Day
    12: COLOUR_LIGHT_GREEN,   # Player's House
}

def colour_text(text, colour):
    return f"{colour}{text}{RESET}"

#func that is the main sorting menu and asks for da stuff
def main_sorting_menu():
    print_header("Plants vs Zombies 2 Database")
    print(f"\n{COLOUR_CYAN}This is a database for PvZ2 plants. Choose how you want to sort by:{RESET}")


    while True:
        print(f"\n{COLOUR_GOLD}Sort Plants By:{RESET}")
        print(f"{COLOUR_GREEN}1.{RESET} View all plants sorted by Sun Cost")
        print(f"{COLOUR_GREEN}2.{RESET} View all plants sorted by Name")
        print(f"{COLOUR_GREEN}3.{RESET} View plants from a specific world sorted by Sun Cost")
        print(f"{COLOUR_GREEN}4.{RESET} View plants from a specific world sorted by Name")
        print(f"{COLOUR_RED}5.{RESET} Exit")

        choice = input(f"{BOLD}Enter your choice (1-5): {RESET}")

        if choice == '1':
            plants = get_all_plants_sorted_by_suncost()
            print_header(colour_text("All Plants by Sun Cost", {COLOUR_GOLD}))
            print(f"{BOLD'Plant Name':<25} | {'Sun Cost':>8} | {'World':<20}")
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
            print("That's not a integer. Please select a number between 1 and 5. NO monkey business like decimals and stuff")


if __name__ == "__main__":
    main_sorting_menu()