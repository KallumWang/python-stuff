import sqlite3

DATABASE = '151 pokemon.db'

def print_all_pokemons():
    Cards = input("How much cards: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Pokemon_name, Cards_made FROM pokemon WHERE Cards_made > ?;"
        cursor.execute(sql,(Cards,))
        results = cursor.fetchall()
        # PRINTS THE DATA NICER
        for pokemon in results:
            print(f"Pokemon: {pokemon[0]} Cards made: {pokemon[1]}")

if __name__ == "__main__":
    print_all_pokemons()
