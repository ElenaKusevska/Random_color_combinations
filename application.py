from flask import Flask, render_template, request, session
from flask_session import Session
import random
import datetime

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
#app.config.from_object(__name__)
Session(app)

ratings = []
text_colors = []
background_colors = []

# Rating page:
@app.route("/")
def index():
    # random seed in some random way
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

@app.route("test")
def test():
    tests = "A"
    return render_template("test.html", tests=tests)

# Confirm page:

@app.route("/confirm", methods=["post"])
def confirm():
    rating = request.form.get("rating")
    text_col = request.form.get("text_col")
    background_col = request.form.get("background_col")
    ratings.append(rating)
    background_colors.append(background_col)
    text_colors.append(text_col)
    tests = "A"

    # Establish connection to local database:
    #conn = sqlite3.connect('./db.sqlite') # Create database
    #cur = conn.cursor()

    # Insert values:
    #current_date_time = str(datetime.datetime.now()).split('.')[0]
    #current_date = current_date_time.split(' ')[0]
    #current_time = current_date_time.split(' ')[1]
     #'INSERT INTO color_combinations_rated (time, date, color1, color2, rating) '
        #+ 'VALUES ( "' + current_date + '", "' + current_time + '", "' + background_col 
        #+ '", "' + text_col'",  ' + str(rating) + ');' )
    #cur.execute(insert_test_value)
    #conn.commit()

    # Close connection:
    #cur.close()
    #conn.close()

    return render_template("confirm.html", background_col=background_col, text_col=text_col, tests=tests,
        rating=rating, ratings=ratings, background_colors=background_colors, text_colors=text_colors)


