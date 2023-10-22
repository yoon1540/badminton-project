import sqlite3

def player_exists(player_name):
    """Check if a player exists in the database."""
    with sqlite3.connect("player.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Name FROM player WHERE Name = ?", (player_name,))
        return cur.fetchone() is not None

def update_elo(player, new_elo):
    """Update the ELO of a player in the database."""
    with sqlite3.connect("player.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE player SET elo = ? WHERE Name = ?", (new_elo, player))
        con.commit()

def elo_recalculation(winner, loser):
    """A simple ELO recalculation. Adjust K, and the algorithm as needed."""
    K = 32
    expected_winner = 1 / (1 + 10**((loser['elo'] - winner['elo']) / 400))
    expected_loser = 1 - expected_winner
    
    winner['elo'] += K * (1 - expected_winner)
    loser['elo'] += K * (0 - expected_loser)

    # Update the new ELO ratings in the database
    update_elo(winner['name'], winner['elo'])
    update_elo(loser['name'], loser['elo'])

def create_match(player1, player2):
    if not player_exists(player1) or not player_exists(player2):
        print("One or both players do not exist in the database. Exiting...")
        return

    while True:
        winner_name = input(f"Who won the match? ({player1} or {player2}): ").strip()
        if winner_name not in [player1, player2]:
            print("Invalid input. Please enter the name of one of the players.")
            continue
        
        with sqlite3.connect("player.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Name, elo FROM player WHERE Name = ?", (player1,))
            player1_data = {'name': player1, 'elo': cur.fetchone()[1]}
            
            cur.execute("SELECT Name, elo FROM player WHERE Name = ?", (player2,))
            player2_data = {'name': player2, 'elo': cur.fetchone()[1]}

        if winner_name == player1:
            elo_recalculation(player1_data, player2_data)
        else:
            elo_recalculation(player2_data, player1_data)

        print(f"ELO updated! {player1}: {int(player1_data['elo'])}, {player2}: {int(player2_data['elo'])}")
        break
