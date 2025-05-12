'''This is code for a Plant's vs Zombies 2 code by Kallum'''
import sqlite3
print("1 = Ancient Egypt")
print("2 = Pirate Seas")
print("3 = Wild West")
print("4 = Frostbite Caves")
print("5 = Lost City")
print("6 = Far Future")
print("7 = Dark Ages")
print("8 = Neon Mixtape Tour")
print("9 = Jurassic Marsh")
print("10 = Big Wave Beach")
print("11 = Modern Day")
print("12 = Player's House")
DATABASE = 'PVZ2.db'

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
