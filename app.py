"""
Author: Kelvin Gooding
Created: 2024-01-18
Updated: 2024-04-11
Version: 1.1
"""

#!/usr/bin/python3

# Modules

from flask import Flask, render_template, request, flash
from modules import db_check
import os

# General Variables

base_path = os.path.expanduser('~/homelab')
app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
db_filename = 'games.db'
sql_script = f'{base_path}/apps/{app_name}/scripts/sql/create_tables.sql'

# SQLite3 Variables

db_check.check_db(os.path.join(f'{base_path}', 'db'), f'{db_filename}', f'{sql_script}')
conn = db_check.sqlite3.connect(os.path.join(base_path, db_filename), check_same_thread=False)
c = conn.cursor()

# Flask Variables

app = Flask(__name__)
app = Flask(__name__)
app.secret_key = os.urandom(26)

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

            return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))

        # Wishlist Filter

        elif 'wishlist' in request.form:

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS5" AND STATUS == "Wishlist" ORDER BY RELEASE_DATE DESC'):
                ps5_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "PS4"  AND STATUS == "Wishlist" ORDER BY RELEASE_DATE DESC'):
                ps4_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            for i in c.execute('SELECT * FROM gamelist WHERE PLATFORM == "Nintendo Switch"  AND STATUS == "Wishlist" ORDER BY RELEASE_DATE DESC'):
                ns_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

            return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))

    # No Filter

    else:

        for i in c.execute('SELECT * FROM gamelist WHERE platform = "PS5" AND status NOT IN ("Wishlist") ORDER BY name ASC;'):
            ps5_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
        for i in c.execute('SELECT * FROM gamelist WHERE platform = "PS4" AND status NOT IN ("Wishlist") ORDER BY name ASC;'):
            ps4_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])

        for i in c.execute('SELECT * FROM gamelist WHERE platform = "Nintendo Switch" AND status NOT IN ("Wishlist") ORDER BY name ASC;'):
            ns_games.append([i[0].upper(), i[1], i[5], i[9], int(i[7])])
        
        return render_template("index.html", ps5_games=ps5_games, ps5_count=len(ps5_games), ps4_games=ps4_games, ps4_count=len(ps4_games), ns_games=ns_games, ns_count=len(ns_games))

@app.route("/new_entry", methods=["POST", 'GET'])
def new_entry():

    status = ['Playing', 'Completed', 'Backlog', 'Wishlist',]
    
    platform = ['PS5', 'PS4', 'Nintendo Switch',]

    format = ['Physical', 'Digital']

    if request.method == "POST":
        c.execute('INSERT INTO gamelist VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (request.form.get("name"), request.form.get("release_date"), request.form.get("players"), request.form.get("genre"), request.form.get("status"), request.form.get("platform"), request.form.get("format"), request.form.get("rating"), request.form.get("link"), request.form.get("cover_image"),))
        conn.commit()

        flash("A new entry has now been added!")
        return render_template("new_entry.html", status=status, platform=platform, format=format)
    
    return render_template("new_entry.html", status=status, platform=platform, format=format)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3008)
