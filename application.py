from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    def choose_color():
        hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        color_list = []
        for i in range(0,6):
            loc = int((random.random()*15.99999999) // 1)
            color_list.append(hexadecimals[loc])
        return "".join(color_list)

    col1 = choose_color()
    col2 = choose_color()
    return render_template("rand_col.html", color1=col1, color2=col2)

