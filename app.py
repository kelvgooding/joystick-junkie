"""
Author: Kelvin Gooding
Created: 2024-01-18
Updated: 2024-01-23
Version: 1.1
"""

#!/usr/bin/python3

from flask import Flask, render_template, request, flash
import sqlite3

# SQLite3 Variables

connection = sqlite3.connect('games.db', check_same_thread=False)
c = connection.cursor()

# Flask Variables

app = Flask(__name__)

@app.route("/" , methods=['POST', 'GET'])
def index():

    # Empty list for each console owned

    ps5_games = []
    ps4_games = []
    ns_games = []

    if request.method == "POST":

        # Clear console lists each time button is pressed.

        ps5_games.clear()
        ps4_games.clear()
        ns_games.clear()

        # Backlog Filter

        if 'backlog' in request.form:

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS5" AND STATUS == "Backlog" ORDER BY NAME ASC'):
                ps5_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS4"  AND STATUS == "Backlog" ORDER BY NAME ASC'):
                ps4_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "Nintendo Switch"  AND STATUS == "Backlog" ORDER BY NAME ASC'):
                ns_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
            
            return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))
        
        # Completed Filter

        elif 'completed' in request.form:

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS5" AND STATUS == "Completed" ORDER BY NAME ASC'):
                ps5_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS4"  AND STATUS == "Completed" ORDER BY NAME ASC'):
                ps4_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "Nintendo Switch"  AND STATUS == "Completed" ORDER BY NAME ASC'):
                ns_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))
        
        # Playing Filter

        elif 'playing' in request.form:

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS5" AND STATUS == "Playing" ORDER BY NAME ASC'):
                ps5_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS4"  AND STATUS == "Playing" ORDER BY NAME ASC'):
                ps4_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "Nintendo Switch"  AND STATUS == "Playing" ORDER BY NAME ASC'):
                ns_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            print(len(ps5_games))

            return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))

    # No Filter

    else:

        for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS5" ORDER BY NAME ASC'):
            ps5_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
        for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS4" ORDER BY NAME ASC'):
            ps4_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

        for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "Nintendo Switch" ORDER BY NAME ASC'):
            ns_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
        return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)