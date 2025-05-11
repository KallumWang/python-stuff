import sqlite3

DATABASE = 'PVZ2.db'

def print_all_Plants():
    World = input("What world unlocked: ")
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
