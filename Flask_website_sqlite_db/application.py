from flask import Flask, render_template, request, session
from flask_session import Session
import sqlite3
import random
import datetime

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

# Get input from user:
@app.route("/")
def index():
    # Add code to random seed in some random way
    # Function to generate two random colors in hexadecimal format:
    def choose_color():
        hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        color_list = []
        for i in range(0,6):
            loc = int((random.random()*15.99999999) // 1)
            color_list.append(hexadecimals[loc]);
        return "".join(color_list)

    text_col = choose_color()
    background_col = choose_color()
    return render_template ("generate_random_colors.html", text_col=text_col, 
        background_col=background_col)

# Register rating provided:
ratings = []
text_colors = []
background_colors = []
@app.route("/confirm", methods=["post"])
def confirm():
    rating = request.form.get("rating")
    text_col = request.form.get("text_col")
    background_col = request.form.get("background_col")
    ratings.append(rating)
    background_colors.append(background_col)
    text_colors.append(text_col)

    # Establish connection to local database:
    conn = sqlite3.connect('./db.sqlite') # Create database
    cur = conn.cursor()

    # Insert values:
    current_date_time = str(datetime.datetime.now()).split('.')[0]
    current_date = current_date_time.split(' ')[0]
    current_time = current_date_time.split(' ')[1]  

    # Insert values to database - method 1
    #inserts = ('INSERT INTO color_combinations_rated (time, date, color1, color2, rating) '
        #+ 'VALUES ( "' + current_date + '", "' + current_time + '", "' + background_col 
        #+ '", "' + text_col + '",  ' + str(rating) + ');' )
    #cur.execute(inserts)

    # Insert values to database - method 2
    #cur.execute( "INSERT INTO color_combinations_rated (time, date, color1, color2, rating) "
        #"VALUES (?, ?, ?, ?, ?)", (current_date, current_time, background_col, text_col, rating) )

    # Insert values to database - method 3
    cur.execute("INSERT INTO color_combinations_rated (time, date, background_col, text_col, rating)" 
        "VALUES (:time, :date, :background_col, :text_col, :rating)",
        {"time": current_time, "date": current_date, "background_col": background_col, "text_col":text_col, "rating": rating})
    conn.commit()

    # Close connection:
    cur.close()
    conn.close()

    return render_template("confirm.html", background_col=background_col, text_col=text_col,
        rating=rating, ratings=ratings, background_colors=background_colors, text_colors=text_colors)

@app.route("/test")
def test():
    testss = "A"
    return render_template("test.html", testss=testss)

@app.route("/tests")
def tests():
    testss = "A"
    return render_template("test.html", testss=testss)