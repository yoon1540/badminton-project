import sqlite3

con = sqlite3.connect("player.db")
cur = con.cursor()


def list_players():
    # Query the database to retrieve the list of players
    cur.execute("SELECT Name, gender, elo, games_played FROM player")
    players = cur.fetchall()
    name_width = max(len(player[0]) for player in players) + 2  # +2 for a little padding
    # Display the list of players
    print("List of Players...\n")
    for player in players:
        name, gender, elo, games_played = player
        elo = int(elo)
        print(f"{name:<{name_width}} | {gender:<6} | {elo:<10} | {games_played:<12}")
        
    print("\n")


def add_player():
    print("====Adding Player====")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    gender = input("Gender (M/F): ")
    full_name = fname + " " + lname
    cur.execute("INSERT INTO player (Name, elo, gender, games_played) VALUES (?, 1000, ?, 0)", (full_name, gender))
    con.commit()

def delete_player():
    name = input("Enter full name of player to delete: ")
    cur.execute("DELETE FROM player WHERE Name=?", (name,))
    con.commit()

def edit_player():
    name = input("Enter full name of player to edit: ")

    # Checking if player exists
    cur.execute("SELECT * FROM player WHERE Name=?", (name,))
    if not cur.fetchone():
        print("Player not found!")
        return

    new_name = input("Enter new full name (press enter to keep current): ")
    new_gender = input("Enter new gender (M/F, press enter to keep current): ")
    new_elo = input("Enter new elo (press enter to keep current): ")

    if new_name:
        cur.execute("UPDATE player SET Name=? WHERE Name=?", (new_name, name))
    if new_gender:
        cur.execute("UPDATE player SET gender=? WHERE Name=?", (new_gender, name))
    if new_elo:
        cur.execute("UPDATE player SET elo=? WHERE Name=?", (new_elo, name))

    con.commit()

def rankings():
    # Query the database to retrieve the top 5 players sorted by ELO in descending order
    cur.execute("SELECT Name, elo FROM player ORDER BY elo DESC LIMIT 5")
    top_players = cur.fetchall()

    # Display the rankings
    print("Top 5 Players by ELO...\n")
    for rank, (name, elo) in enumerate(top_players, 1):  # Enumerate will give us the ranking number
        print(f"{rank}. {name} - {int(elo)}")
    
    print("\n")

