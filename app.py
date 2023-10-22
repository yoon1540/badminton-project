from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_top_players():
    with sqlite3.connect("player.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Name, elo FROM player ORDER BY elo DESC LIMIT 5")
        players = cur.fetchall()
        
    return players

@app.route('/')
def index():
    players = get_top_players()
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)
