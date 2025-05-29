'''This is code for a Plants vs Zombies 2 database by Kallum May 2025'''
import sqlite3

# Constants
DATABASE = 'PVZ2.db'
worlds = {
    1: "Ancient Egypt", 2: "Pirate Seas", 3: "Wild West", 4: "Frostbite Caves", 5: "Lost City", 6: "Far Future", 
    7: "Dark Ages", 8: "Neon Mixtape Tour", 9: "Jurassic Marsh", 10: "Big Wave Beach", 11: "Modern Day", 12: "Player's House"
}

# ANSI escape sequences for 256 colours
RESET = "\033[0m"
BOLD = "\033[1m"

# Colours
COLOUR_GOLD = "\033[38;5;220m"
COLOUR_DARK_BLUE = "\033[38;5;19m"
COLOUR_LIGHT_BROWN = "\033[38;5;180m"
COLOUR_PURPLE = "\033[38;5;93m"
COLOUR_GREY = "\033[38;5;244m"
COLOUR_LIGHT_BLUE = "\033[38;5;117m"
COLOUR_DEEP_GREEN = "\033[38;5;28m"
COLOUR_LIGHT_GREEN = "\033[38;5;120m"
COLOUR_CYAN = "\033[36m"
COLOUR_MAGENTA = "\033[35m"
COLOUR_RED = "\033[31m"
COLOUR_YELLOW = "\033[33m"
COLOUR_GREEN = "\033[32m"
COLOUR_WHITE = "\033[37m"

world_colours = {
    1: COLOUR_GOLD,
    2: COLOUR_DARK_BLUE,
    3: COLOUR_LIGHT_BROWN,
    4: COLOUR_CYAN,
    5: COLOUR_YELLOW,
    6: COLOUR_PURPLE,
    7: COLOUR_GREY,
    8: COLOUR_MAGENTA,
    9: COLOUR_CYAN,
    10: COLOUR_LIGHT_BLUE,
    11: COLOUR_DEEP_GREEN,
    12: COLOUR_LIGHT_GREEN,
}

def colour_text(text, colour):
    return f"{colour}{text}{RESET}"

def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

def print_world_glossary():
    print("World ID Glossary:")
    for id, name in worlds.items():
        print(f"{id:2} = {name}")

# Database functions
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

# Main menu function
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
            print_header(colour_text("All Plants by Sun Cost", COLOUR_GOLD))
            print(f"{'Plant Name':<28} | {'Sun Cost':>8} | {'World':<20}")
            print("-" * 65)
            for name, cost, world_id in plants:
                colour = world_colours.get(world_id, COLOUR_WHITE)
                padded_name = f"{name:<28}"
                coloured_name = colour_text(padded_name, colour)
                print(f"{coloured_name} | {cost:>8} | {worlds.get(world_id, 'Unknown'):<20}")

        elif choice == '2':
            plants = get_all_plants_sorted_by_name()
            print_header("All Plants by Name")
            print(f"{'Plant Name':<28} | {'Sun Cost':>8} | {'World':<20}")
            print("-" * 65)
            for name, cost, world_id in plants:
                colour = world_colours.get(world_id, COLOUR_WHITE)
                padded_name = f"{name:<28}"
                coloured_name = colour_text(padded_name, colour)
                print(f"{coloured_name} | {cost:>8} | {worlds.get(world_id, 'Unknown'):<20}")

        elif choice in ['3', '4']:
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
                print(f"{'Plant Name':<28} | {'Sun Cost':>8}")
                print("-" * 40)
                for name, cost in plants:
                    colour = world_colours.get(world_id, COLOUR_WHITE)
                    padded_name = f"{name:<28}"
                    coloured_name = colour_text(padded_name, colour)
                    print(f"{coloured_name} | {cost:>8}")

        elif choice == '5':
            print("Exiting program")
            break
        else:
            print("That's not an integer. Please select a number between 1 and 5. NO monkey business like decimals and stuff")

if __name__ == "__main__":
    main_sorting_menu()
