from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import os
import random
import datetime

app = Flask(__name__)

# Establish connection to database
app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

print("db", db)

class ColorRating(db.Model):
    __tablename__ = "color_ratings"

    id = db.Column(db.Integer, primary_key=True)
    text_col = db.Column(db.String(7))
    background_col = db.Column(db.String(7))
    rating = db.Column(db.Integer)

    def __init__(self, text_col, background_col, rating):
        self.text_col = text_col
        self.background_col = background_col 
        self.rating = rating


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

    # Get date and time:
    current_date_time = str(datetime.datetime.now()).split('.')[0]
    current_date = current_date_time.split(' ')[0]
    current_time = current_date_time.split(' ')[1]  

    # Insert values to database:
    color_rating = ColorRating(text_col=text_col, background_col=background_col, rating=rating)
    db.session.add(color_rating)
    db.session.commit()

    print(ColorRating.query.all())

    return render_template("confirm.html", background_col=background_col, text_col=text_col,
        rating=rating, ratings=ratings, background_colors=background_colors, text_colors=text_colors)

@app.route("/allratings")
def test():
    all_ratings= ColorRating.query.all()
    return render_template("all_ratings.html", all_ratings=all_ratings)

