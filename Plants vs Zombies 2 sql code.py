'''This is code for a Plants vs Zombies 2 database by Kallum May 2025'''
import sqlite3

# Constants
DATABASE = 'PVZ2.db'
worlds = {
    1: "Ancient Egypt", 2: "Pirate Seas", 3: "Wild West", 4: "Frostbite Caves", 5: "Lost City", 6: "Far Future",
    7: "Dark Ages", 8: "Neon Mixtape Tour", 9: "Jurassic Marsh", 10: "Big Wave Beach", 11: "Modern Day", 12: "Player's House"
}

# Functions
def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

def print_world_glossary():
    print("World ID Glossary:")
    for id, name in worlds.items():
        print(f"{id:2} = {name}")

# Database fetch functions
def get_plants_by_world(world_id, sort_by='Sun_Cost'): #this one sorts by either sun cost or the plants name
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

def get_all_plants_sorted_by_suncost(): #This function sorts plants by sun cost
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Plant_Name, Sun_Cost, World_Unlocked_ID FROM Plants ORDER BY Sun_Cost ASC;"
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def get_all_plants_sorted_by_name(): #this one sorts only by name
    try:
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            sql = "SELECT Plant_Name, Sun_Cost, World_Unlocked_ID FROM Plants ORDER BY Plant_Name ASC;"
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# ANSI colour codes These colours are for the coloured text
RESET = "\033[0m"
BOLD = "\033[1m"

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

def pad_and_colour(text, width, colour, align='left'): #this alligns everything
    if len(text) > width:
        text = text[:width - 3] + '...'
    if align == 'left':
        padded = text.ljust(width)
    elif align == 'right':
        padded = text.rjust(width)
    elif align == 'center':
        padded = text.center(width)
    else:
        padded = text
    return colour_text(padded, colour)

def main_sorting_menu(): #Main sorting menu also prints out a message basically a welcome and explains what the database is and what you want to sort by
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

        if choice == '1': #Choice 1 calls the function where you sort by the suncost
            plants = get_all_plants_sorted_by_suncost()
            print_header(
                f"{pad_and_colour('Plant Name', 25, world_colours[12])} | "
                f"{pad_and_colour('Sun Cost', 9, COLOUR_GOLD, 'center')} | "
                f"{pad_and_colour('World', 20, COLOUR_GOLD)}"
            )
            print("-" * 60)     #this bit is the printing to make it look nicer and add colour also adds lines and stuff
            for name, cost, world_id in plants: 
                colour = world_colours.get(world_id, COLOUR_WHITE)
                plant_name = pad_and_colour(name, 25, colour)
                cost_str = pad_and_colour(str(cost), 9, COLOUR_GOLD, 'center')
                world_name = pad_and_colour(worlds.get(world_id, 'Unknown'), 20, colour)
                print(f"{plant_name} | {cost_str} | {world_name}")

        elif choice == '2': #Choice 2 calls the earlier function and sortbs by names alphabetically
            plants = get_all_plants_sorted_by_name()
            print_header(
                f"{pad_and_colour('Plant Name', 25, world_colours[12])} | "
                f"{pad_and_colour('Sun Cost', 9, COLOUR_GOLD, 'center')} | "
                f"{pad_and_colour('World', 20, COLOUR_GOLD)}"
            )
            print("-" * 60) #same as choice 1 it makeas it look nicer
            for name, cost, world_id in plants:
                colour = world_colours.get(world_id, COLOUR_WHITE)
                plant_name = pad_and_colour(name, 25, colour)
                cost_str = pad_and_colour(str(cost), 9, COLOUR_GOLD, 'center')
                world_name = pad_and_colour(worlds.get(world_id, 'Unknown'), 20, colour)
                print(f"{plant_name} | {cost_str} | {world_name}")

        elif choice in ('3', '4'): #If the user puts either "3" or "4" it prints the world glosssary and then depending on whether they used 3 or 4 it will call a different function
            while True:
                print_world_glossary() #This accepts error so if they do not put a interger from the glossary it will ask again or if they misclick and want to go back they can type b
                user_input = input("Enter World ID (or 'b' to go back): ").strip()
                if user_input.lower() == 'b':
                    break
                try:
                    world_id = int(user_input)
                    if world_id not in worlds:
                        print("WRONG can you even read the glossary try again NO MONKEY BUSINESS Please enter a valid whole number from the glossary.")
                        continue
                    break
                except ValueError:
                    print("WRONG can you even read the glossary try again NO MONKEY BUSINESS Please enter a valid whole number from the glossary.")
                    continue

            if user_input.lower() == 'b':
                continue

            sort_by = 'Sun_Cost' if choice == '3' else 'Plant_Name' #this bit will be the after math after deciding wether the user has put 3 or 4 in and decides on which function to use
            plants = get_plants_by_world(world_id, sort_by)
            if not plants:
                print(f"No plants found in {worlds[world_id]}") #Here just in case database breaks and the worlds lose all their plants and say no plants found in
            else:
                print_header(
                    f"{colour_text(worlds[world_id] + ' Plants Sorted by ' + ('Sun Cost' if sort_by == 'Sun_Cost' else 'Name'), world_colours.get(world_id, COLOUR_WHITE))}"
                )
                print(
                    f"{pad_and_colour('Plant Name', 25, world_colours[12])} | "
                    f"{pad_and_colour('Sun Cost', 9, COLOUR_GOLD, 'center')}"
                )
                print("-" * 36) #This is same as 1 & 2 just here to prit prettier
                for name, cost in plants:
                    plant_name = pad_and_colour(name, 25, world_colours.get(world_id, COLOUR_WHITE))
                    cost_str = pad_and_colour(str(cost), 9, COLOUR_GOLD, 'center')
                    print(f"{plant_name} | {cost_str}")

        elif choice == '5':
            print("Exiting program") #exzits program
            break
        else:
            print("That's not a number from 1 - 5. Please select a number between 1 and 5. NO monkey business like decimals and stuff.")

if __name__ == "__main__":
    main_sorting_menu()

#Explanations for ppl
#Pad_and_colour pads a string and colours the string so they are neat and look nice
