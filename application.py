from flask import Flask, render_template, request, session
from flask_session import Session
import random

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

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
    return render_template("generate_random_colors.html", text_col=text_col, background_col=background_col)

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
    return render_template("confirm.html", background_col=background_col, text_col=text_col, 
        rating=rating, ratings=ratings, background_colors=background_colors, text_colors=text_colors)

