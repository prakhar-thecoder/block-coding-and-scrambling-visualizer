from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/block-coding")
def block_coding():
    return render_template("block_code.html")

@app.route("/scrambling")
def scrambling():
    return render_template("scrambling.html")

if __name__ == "__main__":
    app.run(debug=True)
